import java.net.*; 

import java.io.*; 


	public class Server2 
{ 
	

		private Socket socket = null; 
	
		private ServerSocket server = null; 
	
		private DataInputStream in = null;
		private DataInputStream input = null; 


		private DataOutputStream out = null;	
	
	public Server2(int port) { 
		
	
				try
{ 
			
					server = new ServerSocket(port); 
			
					System.out.println("Server started"); 

			
					System.out.println("Waiting for a client..."); 

			
					socket = server.accept(); 
			
					System.out.println("Welcome!!! You are now connected"); 

			
					in = new DataInputStream(new BufferedInputStream(socket.getInputStream()));
					input = new DataInputStream(System.in);
					out = new DataOutputStream(socket.getOutputStream());			
					String line = "";


					String l="";		
					while (!line.equals("***")|| !l.equals("***")){ 
				
				    		try  
{ 

							
							line = in.readUTF(); 
	
							System.out.println(line);
							l = input.readLine();
							out.writeUTF(l);
					 

		} 
				
						catch(IOException i) 
{ 
					
							System.out.println(i);
								 	
} 

					   		} 
			
					System.out.println("Closing connection"); 
 
			
					socket.close(); 
			
					in.close(); 
				     
} 
		
					
					catch(IOException i) 

							{ 
			
							System.out.println(i); 

							} 
	
				} 

	
					public static void main(String args[]) 
{ 
		
							Server2 server = new Server2(5000); 
	
										} 
			} 
