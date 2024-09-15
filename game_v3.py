def game_core_v3(number: int = 1) -> int:
    """Устанавливаем левую и правую границу и соответственно при каждой итерации, берем точку - середину нашего отрезка,
      и отсекаем ровно половину отрезка не попавшего в область."""

    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0
    left_corner = 0
    right_corner = 100
    trigger = round((left_corner + right_corner )/2 )

    while trigger != number:
      if number > trigger:
        left_corner = trigger
        trigger = round((left_corner + right_corner)/2)
      elif number < trigger:
        right_corner = trigger
        trigger = round((left_corner + right_corner)/2 )

      count +=1

    # Ваш код заканчивается здесь

    return count