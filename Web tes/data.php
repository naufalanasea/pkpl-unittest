<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Form Member</title>
	<link rel="stylesheet" type="text/css" href="form.css">
    <link rel="preconnect" href="https://fonts.gstatic.com">
	<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <section class="header">
		<nav>
			<div class="nav">
				<ul>
                    <li><a href="index.html">Daftar</a></li>
                    <li><a href="menu.html">Home</a></li>
                    <li><a href="data.php">Data Member</a></li>
				</ul>
			</div>
		</nav>

		<div class="text-awal2">
			<h1>Daftar Member</h1>
            <center><table class="table2">
                <tr>
                    <td>No</td>
                    <td>Nama</td>
                    <td>Alamat</td>
                    <td>No Telp</td>
                    <td>Email</td>
                </tr>
                <?php
                    $fp = fopen("form.txt", "r");
                    $i = 1;
                    while ($isi = fgets($fp)) {
                        $pisah = explode("|", $isi);
                        echo "<tr><td>$i</td>";
                        echo "<td>$pisah[0]</td>";
                        echo "<td>$pisah[1]</td>";
                        echo "<td>$pisah[2]</td>";
                        echo "<td>$pisah[3]</td></tr>";
                        $i++;
                    }
                ?>
            </table></center>
        <a href="menu.html" class="button-btn">Daftar Baru</a>
        <a href="hapus.php" class="button1-btn">Hapus File</a>
        </div>
	</section>
</body>
</html>