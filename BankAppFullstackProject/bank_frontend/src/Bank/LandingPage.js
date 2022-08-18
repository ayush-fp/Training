import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
export function LandingPage() {
  let navigate = useNavigate();
  const [user, updateUser] = useState({
    username: "",
    password: "",
    status: false,
  });
  const [username, setUsername] = useState("");
  const [admin, setAdmin] = useState("");

  function usernameChangeHandler(e) {
    let new_user = { ...user };
    new_user.username = e.target.value;
    updateUser(new_user);
  }

  function passwordChangeHandler(e) {
    let new_user = { ...user };
    new_user.password = e.target.value;
    updateUser(new_user);
  }
  function postDataHandler(e) {
    e.preventDefault();
    const getJWTToken = async () => {
      try {
        const resp = await axios.post("http://127.0.0.1:5555/api/v1/login", {
          username: user.username,
          password: user.password,
        });
        await jwtInfo(resp.data);
      } catch (err) {
        console.error(err);
      }
    };
    getJWTToken();
    if (admin == "True") {
      navigate("/admin/home");
    } else if (admin == "False") {
      navigate("/home");
    }
  }

  async function jwtInfo(access_token) {
    try {
      const resp = await axios("http://127.0.0.1:5555/jwtInfo", {
        method: "post",
        headers: { Authorization: `Bearer ${access_token}` },
      });
      setData(resp.data);
    } catch (err) {
      console.error(err);
    }

    localStorage.clear();
    localStorage.setItem("jwt_token", access_token);
  }

  function setData(data) {
    setAdmin(data.isAdmin);
    setUsername(data.username);
  }

  return (
    <center>
      <div className="card" style={{ width: 500, padding: 50, marginTop: 50 }}>
        <h4>Signup</h4>
        <br></br>
        <form onSubmit={postDataHandler}>
          Enter username:{" "}
          <input
            className="form-control"
            type="text"
            value={user.username}
            onChange={usernameChangeHandler}
            required
          />
          <br></br>
          <br></br>
          Enter password:{" "}
          <input
            className="form-control"
            type="text"
            value={user.password}
            onChange={passwordChangeHandler}
            required
          />
          <br></br>
          <br></br>
          <input className="btn btn-danger" type="submit" />
        </form>

        <br></br>
      </div>
    </center>
  );
}
