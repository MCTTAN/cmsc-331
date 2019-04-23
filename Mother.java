public interface Mother {
  public String GetHairColor();
  default String FetEyeColor()
  {
    return EyeColor;
  }
  final String EyeColor = "Blue";
}
