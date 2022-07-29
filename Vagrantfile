# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box_check_update = false
  config.vm.box = "alvistack/centos-8-stream"

  config.vm.provision "ansible" do |ansible|
    ansible.become = true
    ansible.playbook = "playbook.yml"
    ansible.verbose = "v"
    ansible.vault_password_file = "vp"   
  end

  config.vm.network "forwarded_port", guest: 80, host: 8080

end
