const text = [
	{
		text: "Entering power calibration mode",
		filename: "start_calibration_power.mp3",
	},
	{
		text: "Calibrating right power.",
		filename: "right_calibration_start.mp3",
	},
	{ text: "Calibrating left power.", filename: "left_calibration_start.mp3" },
	{
		text: "Right power calibration completed. Please switch the power meter to the left for further calibration.",
		filename: "right_calibration_ok.mp3",
	},
	{
		text: "Power calibration completed, system restarting.",
		filename: "calibration_ok_restart.mp3",
	},
	{
		text: "Entering standard current mode",
		filename: "standard_power_mode.mp3",
	},
	{
		text: "Standard current completed, system restarting.",
		filename: "standard_ok_restart.mp3",
	},
	{ text: "Entering aging mode", filename: "start_aging_mode .mp3" },
	{ text: "System aging, power", filename: "system_aging_power.mp3" },
	{ text: "Status code", filename: "state_code_number.mp3" },
	{
		text: "System upgrade initiated, estimated to take thirty seconds. The device will automatically restart after the upgrade is completed. Please wait.",
		filename: "system_upgrade_restart.mp3",
	},
	{
		text: "System upgrade completed",
		filename: "system_upgrade_complete.mp3",
	},
	{ text: 0, filename: "number_code_zero.mp3" },
	{ text: 1, filename: "number_code_one.mp3" },
	{ text: 2, filename: "number_code_two.mp3" },
	{ text: 3, filename: "number_code_three.mp3" },
	{ text: 4, filename: "number_code_four.mp3" },
	{ text: 5, filename: "number_code_five.mp3" },
	{ text: 6, filename: "number_code_six.mp3" },
	{ text: 7, filename: "number_code_seven.mp3" },
	{ text: 8, filename: "number_code_eight.mp3" },
	{ text: 9, filename: "number_code_nine.mp3" },
	{ text: "point", filename: "number_code_point.mp3" },
	{
		text: "Device network connection exception, please check the network",
		filename: "connect_abnormal_check.mp3",
	},
	{
		text: "Low battery, please replace the battery in time",
		filename: "battery_low_change.mp3",
	},
	{
		text: "Please burn the mainboard serial number.",
		filename: "please_board_number.mp3",
	},
	{
		text: "Please enter the correct mainboard serial number prefix.",
		filename: "right_board_number.mp3",
	},
	{
		text: "Mainboard serial number burned, the number is .",
		filename: "board_number_complete.mp3",
	},
	{ text: "Calibration self-test started", filename: "check_self_start.mp3" },
	{ text: "Calibration self-test completed", filename: "check_self_end.mp3" },
	{ text: "Entering normal mode", filename: "start_normal_mode .mp3" },
]

console.log(text.length)