import './App.css'
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import ListUserPage from "./pages/ListUserPage"
import CreateUser from './pages/CreateUser';
import EditUser from './pages/EditUser';
function App() {

  return (
    <>
       <div className="vh-100">
    <div className="container">
      <h1 className=" text-center mt-4">Users Manager</h1>
    
      <BrowserRouter>
        <Routes>
            <Route path="/" element={<ListUserPage />} />
            <Route path="/adduser" element={<CreateUser />} />
            <Route path="user/:id/edit" element={<EditUser />} />
        </Routes>
      </BrowserRouter>
    </div>
    </div>
    </>
  )
}

export default App
