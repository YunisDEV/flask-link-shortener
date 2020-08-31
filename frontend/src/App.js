import React from 'react';
import './App.scss'

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = { link: '', createdLink: '' }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }
  handleChange(e) {
    console.log(e.target.value)
    if (e.target) {
      this.setState({ [e.target.name]: e.target.value });
    } else if (e.name && e.value) {
      this.setState({ [e.name]: e.value });
    } else {
      return null;
    }
  }
  async handleSubmit(e) {
    e.preventDefault()
    var res = await fetch('/create', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ linkToRedirect: this.state.link })
    })
    var data = await res.json()
    console.log(data)
  }
  render() {
    return (
      <div className="container">
        <div className="box">
          <form method="POST" onSubmit={this.handleSubmit} className="form">
            <h2>
              Enter link you want to short:
            </h2>
            <input onChange={this.handleChange} placeholder="Link here..." required type="text" name="link" id="link" className="input__link" />
            <div className="btnBx">
              <button type="submit">Short Link</button>
            </div>
            {
              this.state.createdLink ?
                <div>
                  <p>Link is ready:</p>
                  <a href={"http://localhost:9000/" + this.state.createdLink}>{"http://localhost:9000/" + this.state.createdLink}</a>
                </div>
                :
                null
            }
          </form>
        </div>
      </div>
    );
  }
}

export default App;
