# natronset
- natronset is natron python setting for lazypic.

#### Install
```
cd ~ && git clone http://github.com/lazypic/natron
```

#### OCIO설치하고 Natron에 물리기
- OpenColorIO를 다운로드 받습니다.
```
cd ~
git clone https://github.com/imageworks/OpenColorIO-Configs
```

- OSX라면 .bash_profile에 아래줄을 추가합니다.
```
export OCIO=$HOME/OpenColorIO-Configs/aces_1.0.3/config.ocio
```

#### Plugin
![natron_plugins](https://user-images.githubusercontent.com/1149996/47964518-a5628b00-e07e-11e8-86da-1cb59c6e4c96.png)

Natron 사용자는 플러그인을 한곳에 모아서 사용합니다.
https://github.com/NatronVFX/natron-plugins 리포지터리이며,
아래처럼 macOS에서 셋팅하면 자동으로 모든 플러그인이 설치됩니다.

```
sudo mkdir -p "/Library/Application Support/Natron/Plugins"
cd "/Library/Application Support/Natron/Plugins"
sudo git clone https://github.com/NatronGitHub/natron-plugins.git
```

플러그인 업데이트는 다음처럼 진행합니다.
```
cd "/Library/Application Support/Natron/Plugins"
sudo git pull
```

#### 레퍼런스
- http://www.vfxplatform.com

#### info
- homepage : https://natron.inria.fr
- source code : https://github.com/MrKepzie/Narton
- python api : https://natron.readthedocs.org/en/workshop/startupscripts.html#examples
