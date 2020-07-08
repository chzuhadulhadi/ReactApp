import { useState } from 'react';
import './App.css';

const CoworkerList = (props) => {
  const statuses = ["Not in Office", "In Office"];
  const [inOffice, setinOffice] = useState(new Array(props.CoworkerList.length).fill(statuses[0]));
  console.log(inOffice);
  function changestatus(i) {

    let tempOff = inOffice.slice();

    if (tempOff[i] === statuses[0]) { tempOff[i] = statuses[1] }
    else { tempOff[i] = statuses[0] }
    console.log(tempOff);
    setinOffice(tempOff);
  }
  return <>
    <table style={{border:"1px solid",alignContent:"center",margin:"auto"}}>
      <tr >
        <th style={{border:"1px solid"}}>First Name</th>
        <th style={{border:"1px solid"}}>Last Name</th>
        <th style={{border:"1px solid"}}>Status</th>
        <th style={{border:"1px solid"}}>Set Status</th>
      </tr>
      {
        props.CoworkerList.map(function (user, i) {
          return (
            <tr key={i}>
              <td style={{border:"1px solid"}}>{user.first_name}</td>
              <td style={{border:"1px solid"}}>{user.last_name}</td>
              <td style={{border:"1px solid"}}>{inOffice[i]}</td>
              <td style={{border:"1px solid"}}><button style={{ margin: "20px 0px", color: "white", background: "black", borderRadius: "5px", padding: "10px 10px", width: "150px" }} onClick={() => { changestatus(i) }}>{inOffice[i] == statuses[0] ? statuses[1] : statuses[0]}</button></td>
            </tr>);
        })
      }
    </table>
  </>
};


export default CoworkerList;
