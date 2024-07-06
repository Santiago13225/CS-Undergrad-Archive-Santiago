package composite;

public class FaxNumber implements Distribution{
	private String name;
	private String faxNumber;

	public FaxNumber(String name, String faxNumber) {
		this.name = name;
		this.faxNumber = faxNumber;
	}

	public void sendMessage(String msg) {
		System.out.printf("%s Fax Number: %s %s\n", this.name, this.faxNumber, msg);
	}
}
