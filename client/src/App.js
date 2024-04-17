import { useContext } from 'react'
import { Outlet } from 'react-router-dom'
import { UserContext } from './context/UserContext'
import Nav from './components/Nav'
import Footer from './components/Footer'

const App = () => {
  const { user } = useContext(UserContext)

    const useAuth = () => {
        return useContext(UserContext)
    }

    const AuthStatus = () => {
        const auth = useAuth()

        if (!auth.user) {
            return 'not logged in!'
        }
        return <p>Welcome {user}.</p>
    }


  return (
		<main>
         <Nav />
         <AuthStatus />
         <Outlet context={{ user }} />
         <Footer />
		</main>
)}

export default App