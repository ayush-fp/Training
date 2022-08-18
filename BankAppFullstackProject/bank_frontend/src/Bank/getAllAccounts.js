import axios from "axios";
import React, { useState, useEffect } from "react";

const baseURL = "http://127.0.0.1:5555/api/v1/admin/getAllUsers";

export default function GetAllUsers() {
  const [post, setPost] = useState([]);

  const [msg, updateMsg] = useState("");
  var isAdmin = "";
  const jwtToken = localStorage.getItem("jwt_token");

  const validate = async () => {
    try {
      if (jwtToken == null) {
        updateMsg("Not Authorized");
        return;
      }
      const resp = await axios("http://127.0.0.1:5555/jwtInfo", {
        method: "post",
        headers: { Authorization: `Bearer ${jwtToken}` },
      });
      isAdmin = resp.data.isAdmin;
      console.log(isAdmin);
      if (isAdmin == "False" || isAdmin == "") {
        updateMsg("Not Authorized");
        return;
      }
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    validate();
    axios
      .get(`${baseURL}`, {
        headers: { Authorization: `Bearer ${jwtToken}` },
      })
      .then((response) => {
        setPost(response.data);
      });
  }, []);

  if (msg == "Not Authorized") {
    return (
      <>
        <center>
          <a href="/">
            <h1>LOGIN AGAIN</h1>
          </a>
        </center>
      </>
    );
  }

  return (
    <div>
      <h1>All Users</h1>

      <table className="table ">
        <thead>
          <tr>
            <th scope="col">UserName</th>
            <th scope="col">Balance</th>
          </tr>
        </thead>
        <tbody>
          {post.map((users, index) => (
            <tr key={index}>
              <td>{users.username}</td>
              <td>{users.balance}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
