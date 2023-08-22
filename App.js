import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./component/Navbar";
import Mybag from "./component/Mybag";
import Payment from "./component/Payment";
import Error from "./component/Error";
import Register from "./component/Register";
import Userdetail from "./component/Userdetail";
import MyOrder from "./component/MyOrder";
import Index from "./component/Index";
import Update_user from "./component/Update_user";
import Login from "./component/Login";
import { createContext, useEffect, useState } from "react";
import Home from "./component/Home";
import Lovelist from "./component/Lovelist";
import Reviews from "./component/Reviews";
import Product_view from "./component/Product_view";
import Forgot_password from "./component/Forgot_password";
import Successfull from "./component/Successfull";
import Admin_register from "./component/Admin_register";
import Admin_panel_Login from "./component/Admin_panel_Login";
import Admin_front_page from "./Restaurant_Admin/Admin_front_page";
import Admin_panel_Navbar from "./Restaurant_Admin/Admin_panel_Navbar";
import Add_product from "./Restaurant_Admin/Add_product";
import Product_update from "./Restaurant_Admin/Product_update";
import Order from "./Restaurant_Admin/Order";


export const global = createContext();

function App() {

  useEffect(()=>{
    if (localStorage.getItem('Restaurant_user_token') !== null  ) 
    {
      var retrievedObject = localStorage.getItem('Restaurant_user_token');
      let data=JSON.parse(retrievedObject)
      Setadmin_data(data)
    }
  },[])

  const [mobile,setmobile]=useState("");
  const [update,setupdate]=useState("normal");
  const [location,setlocation]=useState("");
  const [admin_data,setadmin_data]=useState([]);
  function Setadmin_data(data)
  {
    setadmin_data(data)
  }
  function locationfunction(data)
  {
    setlocation(data);
  }
  function solve_Food(mobile)
  {
    setmobile(mobile);
  }
  function updateData(data)
  {
    setupdate(data);
  }
  return (
    <div className="App">
    {
      admin_data!=undefined && admin_data.length==0?
      <global.Provider value={{Mobile:mobile,Function:solve_Food,child:updateData,update,location:locationfunction,Location:location,Setadmin_data:Setadmin_data}}>
        <Router>
          <Navbar />
          <Routes>
            <Route path="/" element={<Home />}></Route>
            <Route path="/index" element={<Index />}></Route>
            <Route path="Mybag" element={<Mybag />}></Route>
            <Route path="Mybag/:rupes/Payment" element={<Payment/>}></Route>
            <Route path="Register" element={<Register />}></Route>
            <Route path="Login" element={<Login />}></Route>
            <Route path="User/Dashboard" element={<Userdetail/>}></Route>
            <Route path="/MyOrder" element={<MyOrder/>}></Route>
            <Route path="/update/detail" element={<Update_user/>}></Route>
            <Route path="/lovelist" element={<Lovelist/>}></Route>
            <Route path="/Reviews/order_id/:order_id/product_id/:product_id" element={<Reviews/>}></Route>
            <Route path="/product_id/:id" element={<Product_view />} ></Route>
            <Route path="/forgot_password" element={<Forgot_password/>}></Route>
            <Route path="successfull_message" element={<Successfull/>}></Route>
            <Route path="Admin_panel_Login" element={<Admin_panel_Login/>}></Route>
            <Route path="Admin_Register" element={<Admin_register/>}></Route>
            <Route path="*" element={<Error />}></Route>
          </Routes>
        </Router>
      </global.Provider>
    :
      <global.Provider value={{Admin_data:admin_data,Setadmin_data:Setadmin_data}}>
             <Router>
              <Admin_panel_Navbar/>
                <Routes>
                    <Route path="Admin_front_page" element={<Admin_front_page/>}></Route>
                    <Route path="product_add" element={<Add_product/>}></Route>
                    <Route path="product/update/:id" element={<Product_update/>}></Route>
                    <Route path="/order" element={<Order/>}></Route>
                    <Route path="*" element={<Error />}></Route>
                </Routes>
             </Router>
      </global.Provider>


      }
    </div>
  );
}

export default App;
