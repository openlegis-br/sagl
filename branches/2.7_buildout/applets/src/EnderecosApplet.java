import java.applet.*;
import java.awt.Graphics;
import java.io.IOException;
import java.net.Socket;
import java.net.SocketException;
import java.net.InetAddress;

import java.security.AccessController;
import java.security.PrivilegedAction;
import java.security.PrivilegedActionException;
import java.util.Enumeration;
import java.util.ArrayList;
import java.net.NetworkInterface;

 
public class EnderecosApplet extends Applet {

    public static String sep = ":";
    public static String format = "%02X";

    public String getIpAddressInternal() {
        String s1 = "unknown";
        String s2 = getDocumentBase().getHost();
        int port = 80;
        if(getDocumentBase().getPort()!=-1)
            port = getDocumentBase().getPort();

    	try {

    	    String ip = (new Socket(s2, port)).getLocalAddress().getHostAddress();

    		return ip;
        } catch(IOException io){
    		System.out.println(io.getMessage());
   	    }

        return "undefined";
    }

    private final class IpAddressService implements PrivilegedAction<String>
	{
		public String run()
		{
			return getIpAddressInternal();
		}
	}

	public String getIpAddress() throws PrivilegedActionException
    	{
    		return AccessController.doPrivileged( new IpAddressService() );
    	}

    public static String macToString( NetworkInterface ni ) throws SocketException
        {
            return macToString( ni, EnderecosApplet.sep,  EnderecosApplet.format );
        }

    public static String macToString( NetworkInterface ni, String separator, String format ) throws SocketException
        {
            byte mac [] = ni.getHardwareAddress();

            if( mac != null ) {
                StringBuffer macAddress = new StringBuffer( "" );
                String sep = "";
                for( byte o : mac ) {
                    macAddress.append( sep ).append( String.format( format, o ) );
                    sep = separator;
                }
                return macAddress.toString();
            }

            return null;
        }

    protected static String getMacAddressInternal()
    	{
    		try {
    			Enumeration<NetworkInterface> nis = NetworkInterface.getNetworkInterfaces();

    			// not all interface will have a mac address for instance loopback on windows
    			while( nis.hasMoreElements() ) {
    				String mac = macToString( nis.nextElement() );
    				if( mac != null && mac.length() > 0 )
    					return mac;
    			}
    		} catch( SocketException ex ) {
    			System.err.println( "SocketException:: " + ex.getMessage() );
    			ex.printStackTrace();
    		} catch( Exception ex ) {
    			System.err.println( "Exception:: " + ex.getMessage() );
    			ex.printStackTrace();
    		}

    		return "undefined";
    	}

    public static String [] getMacAddresses()
        {
            try {
                Enumeration<NetworkInterface> nis = NetworkInterface.getNetworkInterfaces();

                ArrayList<String> macs = new ArrayList<String>();
                while( nis.hasMoreElements() ) {
                    String mac = macToString( nis.nextElement() );
                    // not all interface will have a mac address for instance loopback on windows
                    if( mac != null ) {
                        macs.add( mac );
                    }
                }
                return macs.toArray( new String[macs.size()] );
            } catch( SocketException ex ) {
                System.err.println( "SocketException:: " + ex.getMessage() );
                ex.printStackTrace();
            } catch( Exception ex ) {
                System.err.println( "Exception:: " + ex.getMessage() );
                ex.printStackTrace();
            }

            return new String[0];
        }

    private final class MacAddressService implements PrivilegedAction<String>
        {
        	public String run()
        	{
            	return getMacAddressInternal();
        	}
        }
    public String getMacAddress() throws PrivilegedActionException
    	{
    		return AccessController.doPrivileged( new MacAddressService() );
    	}


}