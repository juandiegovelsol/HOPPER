// main.js
// Tipos de nodos
const NODE_TYPES = {
  RECTANGLE: "rectangle",
  DIAMOND: "diamond",
  ELLIPSE: "ellipse",
};

// Estado de la aplicación
const state = {
  nodes: [],
  connections: [],
  selectedNode: null,
  dragOffset: { x: 0, y: 0 },
  isConnecting: false,
  startConnector: null,
  canvas: null,
  ctx: null,
};

// Inicialización
function init() {
  state.canvas = document.getElementById("flowchart-canvas");
  state.ctx = state.canvas.getContext("2d");

  // Ajustar tamaño del canvas
  resizeCanvas();
  window.addEventListener("resize", resizeCanvas);

  // Eventos del canvas
  state.canvas.addEventListener("mousedown", handleMouseDown);
  state.canvas.addEventListener("mousemove", handleMouseMove);
  state.canvas.addEventListener("mouseup", handleMouseUp);

  // Botones de la toolbar
  document
    .getElementById("add-rectangle")
    .addEventListener("click", () => addNode(NODE_TYPES.RECTANGLE));
  document
    .getElementById("add-diamond")
    .addEventListener("click", () => addNode(NODE_TYPES.DIAMOND));
  document
    .getElementById("add-ellipse")
    .addEventListener("click", () => addNode(NODE_TYPES.ELLIPSE));
  document
    .getElementById("connect-mode")
    .addEventListener("click", toggleConnectMode);
  document
    .getElementById("export-btn")
    .addEventListener("click", exportAsImage);
  document.getElementById("clear-btn").addEventListener("click", clearCanvas);

  // Render inicial
  render();
}

function resizeCanvas() {
  const container = document.querySelector(".canvas-container");
  state.canvas.width = container.clientWidth;
  state.canvas.height = container.clientHeight;
  render();
}

// Añadir un nuevo nodo
function addNode(type) {
  const newNode = {
    id: Date.now(),
    type,
    x: state.canvas.width / 2 - 50,
    y: state.canvas.height / 2 - 25,
    width: 100,
    height: 50,
    text: type.charAt(0).toUpperCase() + type.slice(1),
    connectors: [
      { id: 1, position: "top" },
      { id: 2, position: "right" },
      { id: 3, position: "bottom" },
      { id: 4, position: "left" },
    ],
  };

  state.nodes.push(newNode);
  render();
}

// Dibujar un nodo
function drawNode(node) {
  state.ctx.fillStyle = "#f8f9fa";
  state.ctx.strokeStyle = "#3498db";
  state.ctx.lineWidth = 2;

  switch (node.type) {
    case NODE_TYPES.RECTANGLE:
      state.ctx.beginPath();
      state.ctx.rect(node.x, node.y, node.width, node.height);
      break;
    case NODE_TYPES.DIAMOND:
      state.ctx.beginPath();
      state.ctx.moveTo(node.x + node.width / 2, node.y);
      state.ctx.lineTo(node.x + node.width, node.y + node.height / 2);
      state.ctx.lineTo(node.x + node.width / 2, node.y + node.height);
      state.ctx.lineTo(node.x, node.y + node.height / 2);
      state.ctx.closePath();
      break;
    case NODE_TYPES.ELLIPSE:
      state.ctx.beginPath();
      state.ctx.ellipse(
        node.x + node.width / 2,
        node.y + node.height / 2,
        node.width / 2,
        node.height / 2,
        0,
        0,
        Math.PI * 2
      );
      break;
  }

  state.ctx.fill();
  state.ctx.stroke();

  // Dibujar texto
  state.ctx.fillStyle = "#333";
  state.ctx.font = "14px Arial";
  state.ctx.textAlign = "center";
  state.ctx.textBaseline = "middle";
  state.ctx.fillText(
    node.text,
    node.x + node.width / 2,
    node.y + node.height / 2
  );

  // Dibujar conectores (solo en modo conexión)
  if (state.isConnecting) {
    node.connectors.forEach((connector) => {
      const { x, y } = getConnectorPosition(node, connector);
      state.ctx.fillStyle = "#e74c3c";
      state.ctx.beginPath();
      state.ctx.arc(x, y, 5, 0, Math.PI * 2);
      state.ctx.fill();
    });
  }
}

// Obtener posición de un conector
function getConnectorPosition(node, connector) {
  switch (connector.position) {
    case "top":
      return { x: node.x + node.width / 2, y: node.y };
    case "right":
      return { x: node.x + node.width, y: node.y + node.height / 2 };
    case "bottom":
      return { x: node.x + node.width / 2, y: node.y + node.height };
    case "left":
      return { x: node.x, y: node.y + node.height / 2 };
    default:
      return { x: node.x, y: node.y };
  }
}

// Dibujar conexiones
function drawConnection(connection) {
  const fromNode = state.nodes.find((n) => n.id === connection.from.nodeId);
  const toNode = state.nodes.find((n) => n.id === connection.to.nodeId);

  if (!fromNode || !toNode) return;

  const fromPos = getConnectorPosition(fromNode, connection.from.connector);
  const toPos = getConnectorPosition(toNode, connection.to.connector);

  // Dibujar línea
  state.ctx.strokeStyle = "#7f8c8d";
  state.ctx.lineWidth = 2;
  state.ctx.beginPath();
  state.ctx.moveTo(fromPos.x, fromPos.y);
  state.ctx.lineTo(toPos.x, toPos.y);
  state.ctx.stroke();

  // Dibujar punta de flecha
  drawArrowHead(fromPos.x, fromPos.y, toPos.x, toPos.y);
}

// Dibujar punta de flecha
function drawArrowHead(fromX, fromY, toX, toY) {
  const headLength = 10;
  const angle = Math.atan2(toY - fromY, toX - fromX);

  state.ctx.fillStyle = "#7f8c8d";
  state.ctx.beginPath();
  state.ctx.moveTo(toX, toY);
  state.ctx.lineTo(
    toX - headLength * Math.cos(angle - Math.PI / 6),
    toY - headLength * Math.sin(angle - Math.PI / 6)
  );
  state.ctx.lineTo(
    toX - headLength * Math.cos(angle + Math.PI / 6),
    toY - headLength * Math.sin(angle + Math.PI / 6)
  );
  state.ctx.closePath();
  state.ctx.fill();
}

// Renderizar todo
function render() {
  // Limpiar canvas
  state.ctx.clearRect(0, 0, state.canvas.width, state.canvas.height);

  // Dibujar conexiones primero (para que queden detrás de los nodos)
  state.connections.forEach(drawConnection);

  // Dibujar nodos
  state.nodes.forEach(drawNode);

  // Si estamos en medio de una conexión, dibujar la línea temporal
  if (state.isConnecting && state.startConnector) {
    const fromNode = state.nodes.find(
      (n) => n.id === state.startConnector.nodeId
    );
    const fromPos = getConnectorPosition(
      fromNode,
      state.startConnector.connector
    );

    state.ctx.strokeStyle = "#3498db";
    state.ctx.lineWidth = 2;
    state.ctx.setLineDash([5, 5]);
    state.ctx.beginPath();
    state.ctx.moveTo(fromPos.x, fromPos.y);
    state.ctx.lineTo(state.currentMousePos.x, state.currentMousePos.y);
    state.ctx.stroke();
    state.ctx.setLineDash([]);
  }
}

// Manejadores de eventos del mouse
function handleMouseDown(e) {
  const rect = state.canvas.getBoundingClientRect();
  const mouseX = e.clientX - rect.left;
  const mouseY = e.clientY - rect.top;

  if (state.isConnecting) {
    // Buscar si se hizo clic en un conector
    for (const node of state.nodes) {
      for (const connector of node.connectors) {
        const { x, y } = getConnectorPosition(node, connector);
        const distance = Math.sqrt((mouseX - x) ** 2 + (mouseY - y) ** 2);

        if (distance < 10) {
          if (!state.startConnector) {
            // Primer conector seleccionado
            state.startConnector = { nodeId: node.id, connector };
          } else if (state.startConnector.nodeId !== node.id) {
            // Segundo conector seleccionado (y no es el mismo nodo)
            state.connections.push({
              from: state.startConnector,
              to: { nodeId: node.id, connector },
            });
            state.startConnector = null;
            render();
          }
          return;
        }
      }
    }

    // Si se hizo clic fuera de un conector, cancelar la conexión
    if (state.startConnector) {
      state.startConnector = null;
      render();
    }
  } else {
    // Buscar si se hizo clic en un nodo para moverlo
    for (let i = state.nodes.length - 1; i >= 0; i--) {
      const node = state.nodes[i];
      if (isPointInNode(mouseX, mouseY, node)) {
        state.selectedNode = node;
        state.dragOffset = {
          x: mouseX - node.x,
          y: mouseY - node.y,
        };
        break;
      }
    }
  }
}

function handleMouseMove(e) {
  const rect = state.canvas.getBoundingClientRect();
  state.currentMousePos = {
    x: e.clientX - rect.left,
    y: e.clientY - rect.top,
  };

  if (state.selectedNode) {
    state.selectedNode.x = state.currentMousePos.x - state.dragOffset.x;
    state.selectedNode.y = state.currentMousePos.y - state.dragOffset.y;
    render();
  } else if (state.isConnecting && state.startConnector) {
    render();
  }
}

function handleMouseUp() {
  state.selectedNode = null;
}

// Verificar si un punto está dentro de un nodo
function isPointInNode(x, y, node) {
  switch (node.type) {
    case NODE_TYPES.RECTANGLE:
      return (
        x >= node.x &&
        x <= node.x + node.width &&
        y >= node.y &&
        y <= node.y + node.height
      );
    case NODE_TYPES.DIAMOND:
      // Fórmula simplificada para diamante
      const centerX = node.x + node.width / 2;
      const centerY = node.y + node.height / 2;
      const dx = Math.abs(x - centerX) / (node.width / 2);
      const dy = Math.abs(y - centerY) / (node.height / 2);
      return dx + dy <= 1;
    case NODE_TYPES.ELLIPSE:
      // Fórmula para elipse
      const rx = node.width / 2;
      const ry = node.height / 2;
      const cx = node.x + rx;
      const cy = node.y + ry;
      return (x - cx) ** 2 / rx ** 2 + (y - cy) ** 2 / ry ** 2 <= 1;
    default:
      return false;
  }
}

// Alternar modo conexión
function toggleConnectMode() {
  state.isConnecting = !state.isConnecting;
  const btn = document.getElementById("connect-mode");
  if (btn) {
    btn.classList.toggle("active", state.isConnecting);
  }

  render();
}

// Exportar como imagen
function exportAsImage() {
  const link = document.createElement("a");
  link.download = "diagrama-flujo.png";
  link.href = state.canvas.toDataURL("image/png");
  link.click();
}

// Limpiar canvas
function clearCanvas() {
  if (window.confirm("¿Estás seguro de que quieres limpiar el diagrama?")) {
    state.nodes = [];
    state.connections = [];
    state.startConnector = null;
    render();
  }
}

// Inicializar la aplicación cuando el DOM esté listo
document.addEventListener("DOMContentLoaded", init);

// Exportar funciones para pruebas
export {
  NODE_TYPES,
  state,
  addNode,
  drawNode,
  getConnectorPosition,
  isPointInNode,
  toggleConnectMode,
  clearCanvas,
};
