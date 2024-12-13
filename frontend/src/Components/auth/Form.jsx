import React from "react";

const Form = ({}) => {
  return (
    <form action="">
      <fieldset>
        <legend> Create Account</legend>
        <div>
          <label htmlFor="email"> Email</label>
          <input type="email" id="email" required />
        </div>
        <div>
          <label htmlFor="password"> Password</label>
          <input type="password" id="password" required />
        </div>
        <div>
          <label htmlFor="password"> Comfirm Password</label>
          <input type="password" id="password" required />
        </div>
        <div>
          <input type="checkbox" required />
          <label htmlFor="checkbox">I accept terms and conditions</label>
        </div>
      </fieldset>
    </form>
  );
};

export default Form;
