<?php
/**********************************************************************
 *
 * $Id: wfs_connector.php,v 1.1 2006/06/14 14:18:54 lbecchi Exp $
 *
 * purpose: This simple php script is used by wfsConnector.js class 
 *
 *
 *
 * author: Lorenzo Becchi & Andrea Cappugi      ominiverdi :-)
 *
 **********************************************************************
 *
 * Copyright (c) 2006, ominiverdi.org
 *
 * Permission is hereby granted, free of charge, to any person obtaining a
 * copy of this software and associated documentation files (the "Software"),
 * to deal in the Software without restriction, including without limitation
 * the rights to use, copy, modify, merge, publish, distribute, sublicense,
 * and/or sell copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included
 * in all copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
 * THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
 * DEALINGS IN THE SOFTWARE.
 *
 **********************************************************************/

/*file vuoto*/
session_start();

header("Content-Type:text/xml");
if (isset($_GET['wpsURL']))  $wpsURL=trim($_GET['wpsURL']);
else {
	echo '<?xml version="1.0" ?><error>connection problem</error>';
	die;
}

if($lines = file($wpsURL)){
	$string = implode('', $lines);
	echo $string;
} else {
	echo '<?xml version="1.0" ?><error>connection problem</error>';
}

?>