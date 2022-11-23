module pratheek(

	input wire A,
	input wire B,
	input wire C,
	input wire D,

	output wire F,
	);
	
	always @(*)
	begin
        F=((B&C)|(A&B&(!D))|(!A)&(!C)&D);  	
	end
	endmodule
