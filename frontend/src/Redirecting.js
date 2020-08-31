import React from 'react'
import './App.scss'
import './Redirecting.scss'

export default class Redirecting extends React.Component {
    constructor(props) {
        super(props)
        this.state = { linkToRedirect: null, inner: (<p></p>) }
    }
    async componentDidMount() {
        let { postfix } = this.props.match.params
        var res = await fetch('/ls/' + postfix)
        console.log(res.status)
        if (res.status == 404) {
            return this.setState({ inner: 'INVALID LINK' })
        } else if (res.status >= 500) {
            return this.setState({ inner: 'SERVER PROBLEM' })
        }
        else if (res.ok) {
            var data = await res.json()
            return this.setState({
                inner: (
                    <div className="success">
                        <p>Link wants to redirect you<br/><b>{data.url}</b></p>
                        <div className="btnBx"><a href={data.url} className="btn">GO</a></div>
                    </div>
                )
            })
        }
    }

    render() {
        return (
            <div className="container" >
                <div className="box"><div>{this.state.inner}</div></div>
            </div>
        )
    }

}
