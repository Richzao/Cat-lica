function verifyDate(data, hora) {
  const agora = new Date();

  const dataHoraConsulta = new Date(`${data}T${hora}`);
  if (isNaN(dataHoraConsulta.getTime())) {
    return false;
  } else if (dataHoraConsulta <= agora) {
    return false;
  }
  return true;
}

function verifyCampo(valor, nomeCampo, campos_invalidos) {
  if (!valor || valor.length === 0) {
    campos_invalidos.push(nomeCampo);
    return true;
  }
  return false;
}

module.exports = { verifyCampo, verifyDate };
