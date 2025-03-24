import {
  BrowserRouter as Router,
  Route,
  Routes,
  useLocation,
} from 'react-router-dom'
import Navbar from './components/Navbar'
import AboutUs from './pages/AboutUs'
import { AnimatePresence } from 'framer-motion'
import Home from './pages/home'
import Login from './components/Login'
import NotFound from './pages/404'
import 'bootstrap/dist/css/bootstrap.min.css'
import CustomUserForm from './components/NewUser'

const AnimatedRoutes = () => {
  const location = useLocation()
  return (
    <AnimatePresence mode="wait">
      <Routes location={location} key={location.key}>
        <Route path="/login" element={<Login />} />
        <Route path="/about" element={<AboutUs />} />
        <Route path="/newuser" element={<CustomUserForm />} />
        <Route path="/" element={<Home />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </AnimatePresence>
  )
}

function App() {
  return (
    <Router>
      <Navbar />
      <div className="container">
        <div className="row">
          <AnimatedRoutes />
        </div>
      </div>
    </Router>
  )
}

export default App
