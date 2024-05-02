import React from "react";
import './main.css';
import { MainView } from "./MainView";
import { Nav } from "./nav/Nav";
import MainViewDash from "./mainview_dash/MainViewDash";
import { useState, useContext, createContext } from "react";

// export const GlobalContext = createContext<GlobalType | undefined>(undefined)

// export type GlobalType = {
//   currentTime: number
//   duration: number
//   pause: boolean
//   login: boolean

//   setCurrentTime: (value:number)=>void
//   setDuration: (value:number)=>void
//   setPause: (value:boolean)=>void
//   setLogin: (value: boolean)=>void
// }
 
function Main() {
    return (
      <div className="main">
        <div className="main-div-holder">
          <MainView/>
          <MainViewDash/>
        </div>
      
    </div>    
  );
}

export default Main;
