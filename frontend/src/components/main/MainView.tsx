import React, { useContext } from 'react'
import { useState  } from 'react';
import { IoMdArrowDropdown } from "react-icons/io";
import { GrContact } from "react-icons/gr";
import { IoReorderThree } from "react-icons/io5";
import logo from "../../logo.svg"
import { GlobalContext } from '../../App';


const MainNav = () => {
  const useCont = useContext(GlobalContext)
  const is_login = useCont!.login
  const [toggle, setToggle] = useState(true)
  
  return (
    <div className="nav-bar-main">
      <div className="left-wilding">
        <span onClick={()=> {
          document.querySelector("#side-main")?.classList.add("show")
        }}><IoReorderThree/></span>
      </div>
      <div className="left-nav">
        <h3>Home</h3>
        <p>Unleash the power of an ultra realistic AI generated audio for your personal uses.</p>
      </div>

      <div className="right-nav">
        <p><span className="currency">Credits:</span> <span className="value">{is_login? 2000: '----'}</span></p>
        <div className='user-dpd dropdown' onClick={()=> {
          if (toggle){
            document.querySelector("#first-dp")?.classList.add("show");
            console.log("False");
            setToggle(false);
          } 
          else {
            document.querySelector("#first-dp")?.classList.remove("show");
            console.log("True");
            setToggle(true);
          }
        }}>
          <p>{is_login? 'lordseidon': 'Guest user'} <span><IoMdArrowDropdown/></span></p> 
          <div className="god-boss" id='first-dp' onClick={()=> {
            document.querySelector('#godboss')?.classList.remove("show")
          }}>
            <div className="dropdown-content" >
              <div className="show-me-pp">
                <img src={logo} alt="Image" />
                 <small>{is_login? 'lodianaselora@gmail.com': 'Guest User'}</small>
              </div>
             
              <a href="#">API Key</a>
              <a href="#">Subscription</a>
              <a href="#">Usage Analytics</a>
              <a href="#">Affiliate </a>
              {is_login? <a href="#">Sign out</a>: ''}
          </div>
          </div>
          
          </div>
      </div>
    </div>
  )
}

export const MainView = () => {
    return (
      <MainNav/>
      )
}
