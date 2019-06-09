def test_config_gen(host):
    host.ansible.get_variables()["features"] = ["bgp", "vlans"]
    host.ansible(
        "include_role",
        module_args={"name": "config_gen"},
        check=False,
    )
    #host.ansible(
    #    "template",
    #    module_args={
    #        "src": "/home/jmcgill/test/anit/anit/roles/config_gen/templates/cisco/defaults/bgp.j2",
    #        "dest": "/home/jmcgill/test/anit/anit/outputs/configs/a.cfg",
    #    },
    #    check=False
    #)
