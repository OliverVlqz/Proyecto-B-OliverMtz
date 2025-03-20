import React, { useState } from "react";
import { login } from "../services/authService";
import { motion } from "framer-motion";
import { Link } from "react-router-dom";


const Login = ({ onLoginSuccess }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      await login(username, password);
      onLoginSuccess();
    } catch (err) {
      setError("Credenciales incorrectas");
    }
  };

  return (
    <motion.div
        initial={{ opacity: 0, y: 50 }}
        animate={{ opacity: 1, y: 0, transition: { duration: 0.5 } }}
        exit={{ opacity: 0, y: -50, transition: { duration: 0.5 } }}
        className="page"
        >
        <div className="d-flex justify-content-center align-items-center vh-100">
            <div className="card p-4 shadow" style={{ width: "350px" }}>
                <h2 className="text-center mb-3">Iniciar sesión</h2>

                {error && <div className="alert alert-danger text-center">{error}</div>}

                <form onSubmit={handleLogin}>
                <div className="mb-3">
                    <label className="form-label">Usuario</label>
                    <input
                    type="text"
                    className="form-control"
                    placeholder="Ingrese su usuario"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    />
                </div>

                <div className="mb-3">
                    <label className="form-label">Contraseña</label>
                    <input
                    type="password"
                    className="form-control"
                    placeholder="Ingrese su contraseña"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    />
                </div>

                <button type="submit" className="btn btn-primary w-100 mb-3">
                    Entrar
                </button>
                
                </form>
                <div className="text-center">
                  <strong>¿No tienes una cuenta?<br></br></strong>
                  <Link className="" to="/register">
                    Registrate
                  </Link>
                </div>
            </div>
    </div>
    
    </motion.div>
  );
};

export default Login;

