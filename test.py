x = """Family Round Signs
Family Round Pedestal Trays
Family Round Tray with Handles
Family Lazy Susans
Family Wreath
Family Wreath
Family Wreath
Family Wreath
Family Wreath
Family Wreath
Family Wreath
Family Wreath
Sports Pallet Signs
Sports Pallet Signs
Sports Pallet Signs
Sports Pallet Signs
Sports Pallet Signs
Sports Lazy Susans
Sports Lazy Susans
Sports Lazy Susans
Roses are Red Taco Dishes MetalWood
Roses are Red Taco Dishes MetalWood
Roses are Red Taco Dishes MetalWood
Roses are Red Taco Dishes MetalWood
Roses are Red Taco Dishes MetalWood
Aztec Quilt METAL & WOOD
Aztec Quilt METAL & WOOD
Friends Gather Here
Football Fans Gather Here PORCH
No Selfies in Bathroom Box
No Selfies in Bathroom Box
Bathroom Escape ONEPIECE
Bathroom Escape ONEPIECE
Soap and Water ONEPIECE
Soap and Water ONEPIECE
Soap and Water ONEPIECE
Soap and Water ONEPIECE
Soap and Water ONEPIECE
Crickets Sing ROUND
Crickets Sing ROUND
Crickets Sing ROUND
Crickets Sing ROUND
Crickets Sing ROUND
Crickets Sing ROUND
Crickets Sing ROUND
Crickets Sing ROUND
Forever One Piece SIgn
Forever One Piece SIgn
Forever One Piece SIgn
Forever One Piece SIgn
Forever One Piece SIgn
Floral Hedgehog ONE PIECE
Floral Hedgehog ONE PIECE
Floral Hedgehog ONE PIECE
Floral Hedgehog ONE PIECE
Floral Hedgehog ONE PIECE
Floral Hedgehog ONE PIECE
Floral Hedgehog ONE PIECE
Floral Hedgehog ONE PIECE
Floral Hedgehog ONE PIECE
May Flowers Quilt ONE PIECE
May Flowers Quilt ONE PIECE
May Flowers Quilt ONE PIECE
May Flowers Quilt ONE PIECE
May Flowers Quilt ONE PIECE
May Flowers Quilt ONE PIECE
May Flowers Quilt ONE PIECE
May Flowers Quilt ONE PIECE
"""

separated_string = x.splitlines()

s = []
for y in separated_string:
    s.append(y.strip())

print(len(s))

print(len(s))
print(len(set(s)))

print(list(set(s)))

# Product with error
product_with_error = ['Sports Lazy Susans', 'Family Lazy Susans', 'Soap and Water ONEPIECE', 'Forever One Piece SIgn',
                      'Family Round Pedestal Trays', 'Family Round Signs', 'Roses are Red Taco Dishes MetalWood',
                      'May Flowers Quilt ONE PIECE', 'Family Round Tray with Handles', 'Sports Pallet Signs',
                      'Aztec Quilt METAL & WOOD', 'Friends Gather Here', 'Bathroom Escape ONEPIECE',
                      'Floral Hedgehog ONE PIECE', 'Family Wreath', 'No Selfies in Bathroom Box', 'Crickets Sing ROUND',
                      'Football Fans Gather Here PORCH']
