import './App.css';
import CoworkerList from './inoutoffice';
function App() {
  const coworkers = [
    { 'first\_name': 'Max', 'last\_name': 'Mustermann' },
    { 'first\_name': 'Vladimir', 'last\_name': 'Leles' },
    { 'first\_name': 'Tobias', 'last\_name': 'Anhalt' },
  ];
  
  return <>
    
    <CoworkerList CoworkerList={coworkers} />
  
      </>

}

export default App;
