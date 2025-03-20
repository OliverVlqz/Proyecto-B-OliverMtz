import React from "react";

const AboutUs = () => {
  return (
    <div className="container mt-5">
      <div className="row align-items-center">
        <div className="col-md-6 text-center">
          <img
            src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Logo-utez.png/300px-Logo-utez.png"
            alt="Sobre Nosotros"
            className="img-fluid rounded shadow "
          />
        </div>

        {/* Texto a la derecha */}
        <div className="col-md-6">
          <h2 className="text-primary">Sobre Nosotros</h2>
          <p className="lead">
            Somos un equipo apasionado por la tecnología y la innovación. Nuestra misión es
            ofrecer soluciones eficientes que mejoren la vida de nuestros usuarios.
          </p>
          <p>
            Con años de experiencia en desarrollo de software, nos especializamos en crear
            aplicaciones modernas, seguras y escalables. Nuestro compromiso es la excelencia
            y la satisfacción del cliente.
          </p>
        </div>
      </div>

      {/* Sección de valores */}
      <div className="row text-center mt-5">
        <h3 className="mb-4 text-secondary">Nuestros Valores</h3>
        <div className="col-md-4">
          <i className="bi bi-lightbulb text-warning" style={{ fontSize: "3rem" }}></i>
          <h4>Innovación</h4>
          <p>Siempre buscamos nuevas formas de mejorar y evolucionar.</p>
        </div>
        <div className="col-md-4">
          <i className="bi bi-heart text-danger" style={{ fontSize: "3rem" }}></i>
          <h4>Pasión</h4>
          <p>Nos encanta lo que hacemos y ponemos el corazón en cada proyecto.</p>
        </div>
        <div className="col-md-4">
          <i className="bi bi-people text-primary" style={{ fontSize: "3rem" }}></i>
          <h4>Trabajo en equipo</h4>
          <p>Creemos en la colaboración para alcanzar grandes objetivos.</p>
        </div>
      </div>

      {/* Sección de contacto */}
      <div className="text-center mt-5">
        <h3 className="text-success">Contáctanos</h3>
        <p>¿Quieres saber más? Escríbenos a <strong>dericklagunes@utez.edu.mx</strong></p>
      </div>
    </div>
  );
};

export default AboutUs;
