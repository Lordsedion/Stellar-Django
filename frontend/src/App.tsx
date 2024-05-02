import React, { createContext, useState } from 'react';
import logo from './logo.svg';
import './App.css';
import Main from './components/main/Main';
import  {Outlet} from 'react-router-dom'
import { Nav } from './components/main/nav/Nav';

export const GlobalContext = createContext<GlobalType | undefined>(undefined)

export type GlobalType = {
  currentTime: number
  duration: number
  pause: boolean
  login: boolean
  audioUrl: string

  setCurrentTime: (value:number)=>void
  setDuration: (value:number)=>void
  setPause: (value:boolean)=>void
  setLogin: (value: boolean)=>void
  setAudioUrl: (value:string)=>void
}

function App() {
  const [currentTime, setCurrentTime] = useState(0)
  const [duration, setDuration] = useState(0)
  const [pause, setPause] = useState(false)
  const [login, setLogin] = useState(false)
  const [audioUrl, setAudioUrl] = useState("");

  return (
    <GlobalContext.Provider value={{currentTime, duration, pause, login, audioUrl,
    setCurrentTime, setDuration, setPause, setLogin, setAudioUrl

    }}>
      <div className="App">
        <Nav/>
        <Outlet/>
    </div>
    </GlobalContext.Provider>
    

  );
}

export default App;
