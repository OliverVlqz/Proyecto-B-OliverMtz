import React, { useState, useEffect } from 'react'
import axios from 'axios'

const CustomUserForm = () => {
  const [formFields, setFormFields] = useState([])
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    name: '',
    surname: '',
    control_number: '',
    age: '',
    tel: '',
  })

  useEffect(() => {
    axios
      .get('http://127.0.0.1:8000/users/form/')
      .then((response) => {
        setFormFields(response.data)
      })
      .catch((error) => {
        console.error('Error al obtener los datos', error)
        alert('Error al obtener los campos del formulario.')
      })
  }, [])

  const handleInputChange = (event) => {
    const { name, value } = event.target
    setFormData({
      ...formData,
      [name]: value,
    })
  }

  const handleSubmit = (event) => {
    event.preventDefault()
    axios
      .post('http://127.0.0.1:8000/users/form/', formData)
      .then((response) => {
        alert(response.data.message)
      })
      .catch((error) => {
        alert('Hubo un error al crear el usuario.')
        console.error('Error al enviar el formulario', error)
      })
  }

  return (
    <div className="container mt-4">
      <h2 className="mb-4 text-center">Registro de nuevo usuario</h2>
      <form onSubmit={handleSubmit}>
        <div className="row">
          {formFields &&
            Object.keys(formFields).map((field) => {
              const { label, input, type } = formFields[field]
              return (
                <div className="col-md-6 mb-3" key={field}>
                  <label htmlFor={input.id} className="form-label">
                    {label}
                  </label>
                  <input
                    {...input}
                    className={`form-control`}
                    value={formData[field] || ''}
                    onChange={handleInputChange}
                    name={field}
                    type={type || 'text'}
                  />

                  {/* Instrucciones si el campo es password */}
                  {field === 'password' && (
                    <div className="form-text text-muted mt-2">
                      <ul className="mb-0 ps-3"></ul>
                    </div>
                  )}
                </div>
              )
            })}
        </div>
        <div className="text-center mt-4">
          <button type="submit" className="btn btn-primary px-5">
            Enviar
          </button>
        </div>
      </form>
    </div>
  )
}

export default CustomUserForm
