// Snippet para mandar dado do HTML/JS para o Flask

document.addEventListener('DOMContentLoaded', () => {
  document.querySelector('button').onclick = () => {
    alert('Welcome, ' + document.querySelector('input').value);//localStorage.getItem('username'));
    const request = new XMLHttpRequest();
    const username = document.querySelector('input').value;
    //
    request.open('POST', '/redirect');
    //
    request.onload = () => {
      alert('okay');
      window.location.href = '/redirect';
    }
    //
  const data = new FormData();
  data.append('username', username);
  request.send(data);
  return false;


//Back-end part

@app.route("/redirect", methods =['POST'])
def redirect():
    username = request.form.get("username")
    print('The username is ' + username)
    return 'Worked'
    #render_template('dashboard.html')
