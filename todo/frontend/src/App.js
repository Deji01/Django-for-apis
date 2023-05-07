import React, {Component} from 'react';
import axios from 'axios';

class App extends Component {
  state = {
    todos: []
  };

  componentDidMount() {
    this.getTodos();
  }

  getTodos() {
    axios
      .get('http://172.16.5.4:8000/api/')
      // .get('https://deji01-turbo-waffle-7x6wv67qp6v2p4pw-8000.preview.app.github.dev/api/')
      .then(res => {
        this.setState({ todos: res.data });
      })
      .catch(err => {
        console.log(err);
      });
  }

  render() {
    return (
        <div>
            {
            this.state.todos.map(item => (
              <div key={item.id}>
                <h1>{item.title}</h1>
                <span>{item.body}</span>
              </div>
            ))}
        </div>
    );
  }
}

export default App;