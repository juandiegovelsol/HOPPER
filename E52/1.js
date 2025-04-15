/**
 * Administra fragmentos de código para varios lenguajes de programación.
 *
 * @author Generado por Code Assistant
 */
const codeSnippetsManager = {
    /**
     * Almacena fragmentos de código.
     * @param {string} id - Identificador único del fragmento.
     * @param {object} details - Detalles del fragmento que incluyen:
     *          - language: Lenguaje de programación.
     *          - description: Descripción del fragmento.
     *          - code: Código del fragmento.
     * @flow | id: string
     * @flow | details: {
     *           language: string;
     *           description: string;
     *           code: string;
     *     }
     */
    addCodeSnippet: (id: string, details: { language: string; description: string; code: string }) => {
        if (!id || typeof id !== 'string' || id.trim() === '') {
            console.error('ID no válido.');
            return;
        }
        if (typeof details !== 'object' || details === null || Array.isArray(details)) {
            console.error('Detalles no válidos.');
            return;
        }
        const { language, description, code } = details;
        if (typeof language !== 'string' || typeof description !== 'string' || typeof code !== 'string') {
            console.error('Detalles no válidos: "language", "description" y "code" deben ser cadenas de texto.');
            return;
        }
        if (code.includes(id)) {
            console.error('El código ya tiene ese ID.');
            return;
        }

        const codeSnippets = codeSnippetsManager.codeSnippets;
        if (codeSnippets) {
            codeSnippets[id] = details;
            console.log(`Fragmento agregado correctamente.`);
        } else {
            console.error('No se puede agregar el fragmento: codeSnippets no está inicializado.');
        }
    },

    /**
     * Recupera un fragmento de código por su ID.
     * @param {string} id - Identificador único del fragmento.
     * @returns {object|string} - El fragmento de código en formato JSON o un mensaje de error si no se encuentra.
     * @flow | id: string
     */
    getCodeSnippet: (id: string) => {
        if (!id || typeof id !== 'string' || id.trim() === '') {
            console.error('ID no válido.');
            return;
        }
        const codeSnippets = codeSnippetsManager.codeSnippets;
        if (codeSnippets && codeSnippets.hasOwnProperty(id)) {
            const snippet = codeSnippets[id];
            return JSON.stringify(snippet, null, 2);
        } else {
            return JSON.stringify({ message: 'Fragmento no encontrado.' });
        }
    },

    /**
     * Enumeración de todos los fragmentos de código para un lenguaje de programación específico.
     * @param {string} language - Lenguaje de programación para filtrar los fragmentos.
     * @returns {Array} - Lista de fragmentos filtrados en formato JSON o un mensaje de error si no se encuentra.
     * @flow | language: string
     */
    listCodeSnippets: (language: string) => {
        if (!language || typeof language !== 'string' || language.trim() === '') {
            console.error('Lenguaje no válido.');
            return;
        }
        const codeSnippets = codeSnippetsManager.codeSnippets;
        if (!codeSnippets) {
            console.error('No se puede listar los fragmentos: codeSnippets no está inicializado.');
            return;
        }
        const filteredSnippets = Object.values(codeSnippets).filter(snippet => snippet.language === language);
        if (filteredSnippets.length === 0) {
            return JSON.stringify({ message: 'No se encontraron fragmentos para el lenguaje especificado.' });
        }
        return JSON.stringify(filteredSnippets, null, 2);
    },

    /**
     * Inicializa el almacenamiento de fragmentos de código.
     * @returns {object} - Objeto con los fragmentos de código inicializados.
     */
    initializeCodeSnippets: () => (codeSnippetsManager.codeSnippets = {}))
};