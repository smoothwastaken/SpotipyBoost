
<p  align="center">

<br>

<a  href=""  rel="noopener">

<img  width=20%  height=20%  src="https://play-lh.googleusercontent.com/P2VMEenhpIsubG2oWbvuLGrs0GyyzLiDosGTg8bi8htRXg9Uf0eUtHiUjC28p1jgHzo"  alt="Spotify Logo"></a>

</p>

  

<h3  align="center">@smoothwastaken/SpotipyBoost</h3>

  

<div  align="center">

  

[![Status](https://img.shields.io/badge/status-development-important.svg)]()

[![GitHub Issues](https://img.shields.io/github/issues/smoothwastaken/SpotipyBoost)](https://github.com/smoothwastaken/SpotipyBoost/issues)

[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/smoothwastaken/SpotipyBoost)](https://github.com/smoothwastaken/SpotipyBoost/pulls)

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

  

</div>

  

---

  

<p  align="center"> A spotify client that boost your stats.

<br>

</p>

  

## 📝 Table of Contents

  

- [About](#about)

- [Getting Started](#getting_started)

- [Usage](#usage)

- [Authors](#authors)

- [Acknowledgments](#acknowledgement) 

<!-- - [Todo](TODO.md) -->

<!-- - [Contributing](CONTRIBUTING.md) -->

  
  

## 🧐 About <a  name = "about"></a>

  

This project was created with the goal of boosting stats.

  

## 🏁 Getting Started <a  name = "getting_started"></a>

  

Install the packages with the command:
`python3 -m pip install -r requirements.txt`

  

<!-- ## 🔧 Contributors

  

See the [To do](TODO.md) for required features to work on.

  

Further information on how to contribute [Here](CONTRIBUTING.md). -->

  

## 🎈 Usage <a  name="usage"></a>

Using this script, you have to create your own app directly on [Spotify Developpers Page](https://developer.spotify.com/dashboard/applications). If you never created a Spotify app before, follow this [guide](). 

When you created your Spotify app, enter the values asked in the `.env_sample` file and follow the instructions.

Also, you have to log onto your spotify account.
> ⚠️ This script will never use your Spotify account to do anything else than detecting the current playing status and starting playing on the idle device used to boost your stats.

So you have to pass your username to start and a `waiting_time` value that will determines the time before the script start playing on the idle device after the last playing interruption.
In order to pass this infos, you have two ways to do it:
 - You pass it directly when executing the script:
```
python3 ./main.py <username> <waiting_time>
```
 - You just launch the script and this infos will be asked.

Then, if you never logged in your Spotify account from the script, you will be ask by Spotify itself to connect. Just connect and you should be able to use SpotipyBoost.

<!-- ## 🚀 Deployment <a name = "deployment"></a>

  

We recommend storing your references in JSON format as it is highly compatible with NoSQL databases and Web Applications. -->

  

## ✍️ Authors <a  name = "authors"></a>

  

- [@smoothwastaken/me](https://github.com/smoothwastaken)

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

  

- [spotipy](https://picoctf.org/) for the amazing python librairy that they provide 