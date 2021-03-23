import java.net.*; 

import java.io.*; 


public class Client2 
{
	// initialize socket and input output streams 
	private Socket socket = null; 
	
	private DataInputStream input = null; 
	
	private DataOutputStream output = null;
	private DataInputStream in = null; 


	
public Client2(String address, int port) 
{ 
	// establish a connection 	
			try
		
				{ 
			
					socket = new Socket(address, port); 
			
					System.out.println("Connected"); 

			
					input = new DataInputStream(System.in); 
			
					output = new DataOutputStream(socket.getOutputStream());
					in = new DataInputStream(new BufferedInputStream(socket.getInputStream()));
		
				} 
		
			catch(UnknownHostException u) 
		
				{ 
			
					System.out.println(u); 
		
				} 
		
			catch(IOException e) 
		
				{ 
			
					System.out.println(e); 
		
				} 
 
		
			String l = ""; 
	String line ="";	
			System.out.println("Enter '***' to disconnect");
 
		
			while (!l.equals("***")||!line.equals("***")) 
{ 
			
			try
			
				{ 
				
					l = input.readLine(); 
				
					output.writeUTF(l); 

					line =in.readUTF();
					System.out.println(line);
			
				} 
			
			catch(IOException e) 
	
				{ 
				
					System.out.println(e);
			
				} 
			
					} 

		
				try
		
					{ 
			
						input.close(); 
			
						output.close();
			
						System.out.println("Closing connection");  
			
						socket.close(); 
		
					} 
		
				catch(IOException e) 
		
					{ 
			
						System.out.println(e);
		
					} 
	
			} 

	
public static void main(String args[]) 
	{ 
		
		Client2 client = new Client2("127.0.0.1",5000); 
	} 

} 
