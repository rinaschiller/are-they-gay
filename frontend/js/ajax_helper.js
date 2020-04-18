// const baseURL = window.location.origin;
// const baseURL = "https://aretheygay.org";
const baseURL = "http://localhost:3000/dev";

function ajaxPost(endp, body) {
  url = baseURL + endp;
  return axios.post(url, body);
}

function ajaxGet(endp, body) {
  url = baseURL + endp;
  return axios.get(url);
}

function apiErrHandler(err) {
  const errMsg = err.messtmlage;

  if (errMsg == 'Request failed with status code 401') {
    window.location.href = baseURL + '/';
  }
}
