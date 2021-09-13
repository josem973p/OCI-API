import oci

config = oci.config.from_file()
conf = []

try:
    f = open("deploymentConf.txt", "r")
    for linea in f:
        conf.append(linea)
      #  print(linea)

    f.close()
except:
    print('eror')

print(conf[0])
print(conf[1])

golden_gate_client = oci.golden_gate.GoldenGateClient(config)


if conf[1]=="1":
    start_deployment_response = golden_gate_client.start_deployment(
    deployment_id="ocid1.goldengatedeployment.oc1.iad.amaaaaaa7rhktwqazs3fvhdjnlsrnjen73oodzqqj6mkvw7tgptoncg2id7q",
    start_deployment_details=oci.golden_gate.models.DefaultStartDeploymentDetails(
        type="DEFAULT"))

    print(start_deployment_response.headers)

elif conf[1]=="2":
    stop_deployment_response = golden_gate_client.stop_deployment(
    deployment_id="ocid1.goldengatedeployment.oc1.iad.amaaaaaa7rhktwqazs3fvhdjnlsrnjen73oodzqqj6mkvw7tgptoncg2id7q",
    stop_deployment_details=oci.golden_gate.models.DefaultStopDeploymentDetails(
        type="DEFAULT"))

    print(stop_deployment_response.headers)














