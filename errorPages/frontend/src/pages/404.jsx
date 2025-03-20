// src/pages/NotFound.jsx
import { Link } from "react-router-dom";

const NotFound = () => {
  return (
    <div className="container text-center mt-5">
      <div className="row">
        <div className="col">
          <h1 className="display-1 text-danger">404</h1>
          <h2>¡Vaya! Página no encontrada</h2>
          <p>La página que estás buscando no existe o ha sido movida.</p>
          <Link to="/" className="btn btn-primary mt-3">
            Volver al inicio
          </Link>
        </div>
      </div>
    </div>
  );
};

export default NotFound;
