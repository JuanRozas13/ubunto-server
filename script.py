#Ubunto server
ip address show
#1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
#    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
#    inet 127.0.0.1/8 scope host lo
#       valid_lft forever preferred_lft forever
#    inet6 ::1/128 scope host
#       valid_lft forever preferred_lft forever
#2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
#    link/ether 08:00:27:58:7f:49 brd ff:ff:ff:ff:ff:ff
#    inet 10.26.44.32/24 metric 100 brd 10.26.44.255 scope global dynamic enp0s3
#       valid_lft 28530sec preferred_lft 28530sec
#    inet6 fe80::a00:27ff:fe58:7f49/64 scope link
#       valid_lft forever preferred_lft forever

#---------------------------------------------------------------------
#O ip ele muda pois ainda não foi configurado para deixar ele estático



#Acessar via ssh no git bash
ssh senac@10.26.44.38

W
# 23:17:30 up 11 min,  2 users,  load average: 0.00, 0.00, 0.00
#USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
#senac    tty1     -                23:12   42.00s  0.04s  0.02s -bash
#senac    pts/0    10.26.44.26      23:17    1.00s  0.01s  0.00s w


#Update é utilizado para baixar informações de pacotes de todas as fontes configuradas.
#opção do comando apt: update (Resynchronize the package index files from their sources)
sudo apt update


#List é utilizado para listar todos os software que serão atualizados no sistema.
#opção do comando apt: list (list is used to display a list of packages), --upgradable (shows
#a list of packages that can be upgraded using the apt package manager)
#opção do redirecionador | (pipe): Conecta a saída padrão com a entrada padrão de outro comando
#opção do comando cat: -n (number line)
sudo apt list --upgradable | cat -n


#Upgrade é utilizado para instalar atualizações disponíveis de todos os pacotes atualmente 
#instalados no sistema a partir das fontes configuradas via sources.list
#opção do comando apt: upgrade (Install the newest versions of all packages currently installed
#on the system from the sources enumerated in /etc/apt/sources.list.)
sudo apt upgrade
  Do you want to continue? [Y/n] y <Enter>

#OBSERVAÇÃO: algumas vezes pode aparecer uma tela na cor: Rosa/Branca informando que alguns
#serviços de rede serão reinicializados, isso é comum na distribuição Ubuntu Server.
Daemons using outdated libraries
  Which services should be restarted?
<OK>


#Dist-Upgrade além de executar a função de atualização, também lida de forma inteligente 
#com as novas dependências das novas versões de pacotes
#opção do comando apt: dist-upgrade (dist-upgrade in addition to performing the function of upgrade, 
#also intelligently handles changing dependencies with new versions of packages)
sudo apt dist-upgrade


#Full-Upgrade executa a função de atualização, mas removerá os pacotes atualmente 
#instalados se isso for necessário para atualizar o sistema como um todo
#opção do comando apt: full-upgrade (Perform the function of upgrade but may also remove installed
#packages if that is required in order to resolve a package conflict)
sudo apt full-upgrade


#Autoremove é utilizado para remover pacotes que foram instalados automaticamente para 
#satisfazer dependências de outros pacotes e agora não são mais necessários, pois as 
#dependências foram alteradas ou os pacotes que precisavam deles foram removidos nesse 
#meio tempo.
#opção do comando apt: autoremove (Autoremove is used to remove packages that were automatically
#installed to satisfy dependencies)
sudo apt autoremove


#Autoclean como Clean, o autoclean limpa o repositório local de arquivos de pacotes 
#recuperados. A diferença é que ele remove apenas arquivos de pacotes que não podem 
#mais ser baixados e são inúteis.
#opção do comando apt: autoclean (Like clean, autoclean clears out the local repository of 
#retrieved package files)
sudo apt autoclean


#Clean limpa o repositório local de arquivos de pacotes recuperados
#opção do comando apt: clean (clean clears out the local repository of retrieved package files)
sudo apt clean


#List é utilizado para listar todos os software que serão atualizados no sistema.
#opção do comando apt: list (list is used to display a list of packages), --installed (shows
#a list of packages names as well as options to list installed)
#opção do redirecionador | (pipe): Conecta a saída padrão com a entrada padrão de outro comando
#opção do comando cat: -n (number line)
sudo apt list --installed | cat -n


#Verificando o Log de instalação e atualização de pacotes no Ubuntu Server
#opção do comando cat: -n (number line)
sudo cat -n /var/log/apt/history.log

#Verificando o Log de finalização da atualização de pacotes no Ubuntu Server
#opção do comando cat: -n (number line)
sudo cat -n /var/log/apt/term.log


#Reiniciar o servidor para testar as atualizações
sudo reboot


#---------------------------- 28/11/25

sudo vim /etc/hosts.deny #não precisa reiniciar o serviço, alterou esta funcionando

# /etc/hosts.deny: list of hosts that are _not_ allowed to access the system.
#
#                  See the manual pages hosts_access(5) and hosts_options(5).
#
# Example:    ALL: some.host.name, .some.domain
#             ALL EXCEPT in.fingerd: other.host.name, .other.domain
#
# If you're going to protect the portmapper use the name "rpcbind" for the
# daemon name. See rpcbind(8) and rpc.mountd(8) for further information.
#
# The PARANOID wildcard matches any host whose name does not match its
# address.
#
# You may wish to enable this to ensure any programs that don't
# validate looked up hostnames still leave understandable logs. In past
# versions of Debian this has been the default.
# ALL: PARANOID
ALL: ALL


primeira coluna: 
serviço

segunda coluna:
redes

terceira coluna
ação

negar ou permitir


negar tudo bloquia tudo e libera por exeção 
libera o que é essencial e bloqueia o resto 

#----------------------------


sudo vim /etc/hosts.allow #não precisa reiniciar o serviço, alterou esta funcionando

  1 # /etc/hosts.allow: list of hosts that are allowed to access the system.
  2 #                   See the manual pages hosts_access(5) and hosts_options(5)    .
  3 #
  4 # Example:    ALL: LOCAL @some_netgroup
  5 #             ALL: .foobar.edu EXCEPT terminalserver.foobar.edu
  6 #
  7 # If you're going to protect the portmapper use the name "rpcbind" for the
  8 # daemon name. See rpcbind(8) and rpc.mountd(8) for further information.
  9 #
 10 sshd: 10.26.44.16
 11 sshd: 10.26.44.200

#----------------------------

senac@wsjuan:~$ sudo cp -v /etc/ssh/sshd_config /etc/ssh/sshd_config.old
'/etc/ssh/sshd_config' -> '/etc/ssh/sshd_config.old'


#----------------------------


senac@wsjuan:~$ sudo wget -v -O /etc/ssh/sshd_config https://raw.githubusercontent.com/vaamonde/ubuntu-2204/main/conf/sshd_config
--2025-11-28 20:04:47--  https://raw.githubusercontent.com/vaamonde/ubuntu-2204/main/conf/sshd_config
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.111.133, 185.199.108.133, 185.199.110.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.111.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 9145 (8,9K) [text/plain]
Saving to: ‘/etc/ssh/sshd_config’

/etc/ssh/sshd_config              100%[===========================================================>]   8,93K  --.-KB/s    in 0s

2025-11-28 20:04:48 (37,9 MB/s) - ‘/etc/ssh/sshd_config’ saved [9145/9145]


#----------------------------


senac@wsjuan:~$ sudo wget -v -O /etc/issue.net https://raw.githubusercontent.com/vaamonde/ubuntu-2204/main/conf/issue.net
--2025-11-28 20:05:08--  https://raw.githubusercontent.com/vaamonde/ubuntu-2204/main/conf/issue.net
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.111.133, 185.199.108.133, 185.199.109.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.111.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1604 (1,6K) [text/plain]
Saving to: ‘/etc/issue.net’

/etc/issue.net                    100%[===========================================================>]   1,57K  --.-KB/s    in 0s

2025-11-28 20:05:08 (4,19 MB/s) - ‘/etc/issue.net’ saved [1604/1604]


#----------------------------


senac@wsjuan:~$ sudo wget -v -O /etc/issue https://raw.githubusercontent.com/vaamonde/ubuntu-2204/main/conf/issue
--2025-11-28 20:05:21--  https://raw.githubusercontent.com/vaamonde/ubuntu-2204/main/conf/issue
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133, 185.199.109.133, 185.199.111.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 404 [text/plain]
Saving to: ‘/etc/issue’

/etc/issue                        100%[===========================================================>]     404  --.-KB/s    in 0s

2025-11-28 20:05:21 (79,8 MB/s) - ‘/etc/issue’ saved [404/404]


#----------------------------


sudo vim /etc/ssh/sshd_config
INSERT

 14 # Incluindo o diretório de configuração personalizada do OpenSSH Server
 15 Include /etc/ssh/sshd_config.d/*.conf
 16 #
 17 # Porta de conexão padrão do Servidor de OpenSSH, por segurança é recomendado mudar
 18 # o número da porta. Caso você mude o número da porta, no cliente você precisa usar
 19 # o comando: ssh -p porta usuário@ip_do_servidor
 20 Port 22
 21 #
 22 # Versão do protocolo padrão do Servidor de OpenSSH
 23 Protocol 2
 24 #
 25 # Endereço IPv4 do Servidor de OpenSSH que está liberado para permitir conexões remotas
 26 # via protocolo SSH (Alterar o valor do endereço IPv4 da sua rede)
 27 ListenAddress 10.26.44.220

 63 # Configuração dos Log's do Servidor de OpenSSH, recomendado utilizar junto com os
 64 # arquivos de configuração: hosts.allow e hosts.deny para geração de log´s detalhados
 65 # das conexões ao Servidor de OpenSSH.
 66 # Log's de autenticação do OpenSSH: sudo cat -n /var/log/auth.log | grep -i sshd
 67 # Log's de serviço do OpenSSH: sudo cat -n /var/log/syslog | grep -i ssh
 68 SyslogFacility AUTH
 69 LogLevel VERBOSE
 70 #
 71 # Negar o acesso remoto ao Servidor de OpenSSH para o usuário ROOT
 72 PermitRootLogin no
 73 #
 74 # Usuários que tem permissão de acesso remoto ao Servidor de OpenSSH, separados por
 75 # espaço, deve existir no servidor. Usuários listados no arquivo /etc/passwd
 76 AllowUsers senac
 77 #
 78 # Grupos que tem permissão de acesso remoto ao Servidor de OpenSSH, cuidado, se você
 79 # usar a variável AllowUsers o grupo padrão do usuário precisa está liberado na linha
 80 # AllowGroups, separados por espaço, deve existir no servidor. Grupos listados no
 81 # arquivo /etc/group
 82 AllowGroups senac

ESC SHIFT :x <Enter>


#----------------------------


sudo sshd -t

sudo vim /etc/issue.net

**************************************************************************
##########################################################################
##          Acesso ao Servidor Remoto utilizando o OpenSSH              ##
##          Servidor: wsseunome - Admin.: Juan Rozas                    ##
##########################################################################
**************************************************************************
     _____               _   _    _____   ______   _____    _   _   _
    |  __ \      /\     | \ | |  / ____| |  ____| |  __ \  | | | | | |
    | |  | |    /  \    |  \| | | |  __  | |__    | |__) | | | | | | |
    | |  | |   / /\ \   | . ` | | | |_ | |  __|   |  _  /  | | | | | |
    | |__| |  / ____ \  | |\  | | |__| | | |____  | | \ \  |_| |_| |_|
    |_____/  /_/    \_\ |_| \_|  \_____| |______| |_|  \_\ (_) (_) (_)
                      WARNING: UNAUTHORIZED USERS
**************************************************************************
AVISO: O acesso nao autorizado a este sistema e proibido e sera processado
conforme a lei.  Ao se conectar nesse sistema,  voce concorda que todas as
suas acoes  serao monitoradas, caso  seja  verificado  o uso  indevido dos
recursos de acesso remoto nesse servidor, sera aplicado a lei vigente  com
base nas diretivas da LGPD (Lei Geral de Protecao de Dados n: 13.709/2018)

**************************************************************************
##########################################################################
**************************************************************************


#----------------------------


