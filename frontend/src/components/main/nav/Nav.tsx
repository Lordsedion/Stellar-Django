import React, { useContext } from 'react'
import "./nav.css"
import { FaHome, FaCode, FaBook, FaMoneyBillWave } from "react-icons/fa";
import { MdOutlineExplore, MdOutlineKeyboardVoice, MdOutlineTranslate, MdPublic} from "react-icons/md";
import { RiAiGenerate } from "react-icons/ri";
import { IoMdSettings } from "react-icons/io";
import { GrContact } from "react-icons/gr";
import { BsQuestionSquareFill } from "react-icons/bs";
import logo from "../../../logo.svg"
import { GlobalContext } from '../../../App';
// import { GlobalContext } from '../Main';



export const Nav = () => {
    const useCont = useContext(GlobalContext)
    const login = useCont!.login

    return (
        <>
        <div className="god-boss-1" id='side-main' onClick={()=> {
            document.querySelector("#side-main")?.classList.remove("show")
        }}>
        <div className="sidebar" id="side-main" >
            <div className="icon-nav">
                <a href="">
                    <img src={logo} alt="logo" />

                </a>
            </div>
            <div className="navbar">
                <div className="first-nav">
                    <a href="#"><span className='nav-icons'><FaHome/></span><span className='dp-on-hover'>Home</span></a>
                    <a href="#"><span className='nav-icons'><MdOutlineExplore/></span><span className='dp-on-hover'>Explore</span></a>
                
                    <a href="#"><span className='nav-icons'><MdOutlineTranslate /></span><span className='dp-on-hover'>History</span></a>
                    {/* <a href="#"><span className='nav-icons'><RiAiGenerate/></span><span className='dp-on-hover'>Generate</span></a> */}
                
                    <a href="#"><span className='nav-icons'><IoMdSettings/></span><span className='dp-on-hover'>Settings</span></a>
                    <a href="#"><span className='nav-icons'><FaMoneyBillWave/></span><span className='dp-on-hover'>Billing</span></a>
                    <a href="#"><span className='nav-icons'><FaCode/></span><span className='dp-on-hover'>API</span></a>
                </div>
                <div className="fourth-nav">
                    <a href="#"><span className='nav-icons'><GrContact/></span><span className='dp-on-hover'>Contact</span></a>
                    <a href="#"><span className='nav-icons'><BsQuestionSquareFill/></span><span className='dp-on-hover'>FAQ</span></a>
                    {/* <a href="#"><span className='nav-icons'><FaBook/></span><span className='dp-on-hover'>Docs</span></a> */}
                    <p className='dp-nav'><a href='#'><img src={logo} alt="logo" /> <p className='dp-on-hover'> 
                    <p>{ login? 'Lord Seidon': "Guest User"}</p>
                    <p className='email-dp'>{login ? 'lodianaselora@gmail.com': 'Guest User'}</p>
                    </p></a></p>
                </div>
                
            </div>
        </div>
        </div>
        <div className="sidebar" id='side-main'>
            <div className="icon-nav">
                <a href="">
                    <img src={logo} alt="logo" />

                </a>
            </div>
            <div className="navbar">
                <div className="first-nav">
                    <a href="#"><span className='nav-icons'><FaHome/></span><span className='dp-on-hover'>Home</span></a>
                    <a href="#"><span className='nav-icons'><MdOutlineExplore/></span><span className='dp-on-hover'>Explore</span></a>
                
                    <a href="#"><span className='nav-icons'><MdOutlineTranslate /></span><span className='dp-on-hover'>History</span></a>
                    {/* <a href="#"><span className='nav-icons'><RiAiGenerate/></span><span className='dp-on-hover'>Generate</span></a> */}
                
                    <a href="#"><span className='nav-icons'><IoMdSettings/></span><span className='dp-on-hover'>Settings</span></a>
                    <a href="#"><span className='nav-icons'><FaMoneyBillWave/></span><span className='dp-on-hover'>Billing</span></a>
                    <a href="#"><span className='nav-icons'><FaCode/></span><span className='dp-on-hover'>API</span></a>
                </div>
                <div className="fourth-nav">
                    <a href="#"><span className='nav-icons'><GrContact/></span><span className='dp-on-hover'>Contact</span></a>
                    <a href="#"><span className='nav-icons'><BsQuestionSquareFill/></span><span className='dp-on-hover'>FAQ</span></a>
                    {/* <a href="#"><span className='nav-icons'><FaBook/></span><span className='dp-on-hover'>Docs</span></a> */}
                    <p className='dp-nav'><a href='#'><img src={logo} alt="logo" /> <p className='dp-on-hover'> 
                    <p>{ login? 'Lord Seidon': "Guest User"}</p>
                    <p className='email-dp'>{login ? 'lodianaselora@gmail.com': 'Guest User'}</p>
                    </p></a></p>
                </div>
                
            </div>
        </div>
        </>
        
    )
}
