// Topbar.jsx
import React, { useEffect, useState } from "react";
import styled from "styled-components";

const TopbarContainer = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background-color: #483c32; /* Color de fondo café */
  color: #f0e68c; /* Color de texto claro para contraste */
`;

const Column = styled.div`
  flex: 1;
  padding: 10px;
  text-align: center;
`;

const Icon = styled.img`
  width: 50px; /* Ajusta el tamaño según sea necesario */
  height: 50px; /* Ajusta el tamaño según sea necesario */
`;

const data = {
  id: 1,
  name: "John Doe",
  profession: "Software Developer",
  subprofession: "Backend Developer",
  title: "Senior Developer",
  email: "john.doe@example.com",
  icon: "avatar.png",
  hp: 100,
  maxHP: 100,
  mana: 50,
  maxMana: 60,
  stamina: 20,
  maxStamina: 100,
  exp: 500,
  maxExp: 1000,
  level: 3,
  money: 1000,
  password: "$2a$10$hVJGwQlWjUyDbHF0jupyjOTpqNDYKyvq3lAh8Ohe69pWDOASkIvvq",
  role: "1",
  failedLoginAttempts: 0,
  active: false,
  locked: false,
};

const Topbar = () => {
  const [userData, setUserData] = useState(null);

  useEffect(() => {
    // Suponiendo que la URL de tu API es /api/user
    const fetchData = async () => {
      try {
        /* const response = await fetch("/api/user");
        const data = await response.json(); */
        setUserData(data);
      } catch (error) {
        console.error("Error fetching user data:", error);
      }
    };

    fetchData();
  }, []);

  if (!userData) return null; // Puedes mostrar un loader aquí si quieres

  return (
    <TopbarContainer>
      <Column>
        <Icon src={`./imagenes/${userData.icon}`} alt="User Icon" />
      </Column>
      <Column>
        <h3>{userData.name}</h3>
        <p>{userData.profession}</p>
        <p>{userData.subprofession}</p>
        <p>{userData.title}</p>
      </Column>
      <Column>
        <p>Nivel: {userData.level}</p>
        <p>
          Experiencia: {userData.exp} / {userData.maxExp}
        </p>
        <p>Dinero: {userData.money}</p>
      </Column>
      <Column>
        <p>
          HP: {userData.hp} / {userData.maxHP}
        </p>
        <p>
          Mana: {userData.mana} / {userData.maxMana}
        </p>
        <p>
          Vitalidad: {userData.stamina} / {userData.maxStamina}
        </p>
      </Column>
    </TopbarContainer>
  );
};

export default Topbar;
