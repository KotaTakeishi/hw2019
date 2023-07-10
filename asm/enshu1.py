from inst import Inst, asm, print_asm, print_ihex

program = [
    # 数字をストア
    Inst.LUI(5, 0x10001000),  # memory = 0x10001000
    Inst.ADDI(6, 0, 0b11111100), # 0
    Inst.SB(5, 6, 0x0),
    Inst.ADDI(6, 0, 0b01100000), # 1
    Inst.SB(5, 6, 0x1),
    Inst.ADDI(6, 0, 0b11011010), # 2
    Inst.SB(5, 6, 0x2),
    Inst.ADDI(6, 0, 0b11110010), # 3
    Inst.SB(5, 6, 0x3),
    Inst.ADDI(6, 0, 0b01100110), # 4
    Inst.SB(5, 6, 0x4),
    Inst.ADDI(6, 0, 0b10110110), # 5
    Inst.SB(5, 6, 0x5),
    Inst.ADDI(6, 0, 0b10111110), # 6
    Inst.SB(5, 6, 0x6),
    Inst.ADDI(6, 0, 0b11100000), # 7
    Inst.SB(5, 6, 0x7),
    Inst.ADDI(6, 0, 0b11111110), # 8
    Inst.SB(5, 6, 0x8),
    Inst.ADDI(6, 0, 0b11110110), # 9
    Inst.SB(5, 6, 0x9),

    # Main
    Inst.LUI(12, 0x04000000),
    Inst.ADDI(6, 12, 0x01),
    Inst.ADD(7, 0, 0), # x7 = 0 (counter)
    Inst.ADD(11, 0, 0), # x11 = 0 (counter)
    'loop',
    Inst.ADD(8, 7, 5), # address of memory[x7]
    Inst.ADD(13, 11, 5), # address of memory[x11]
    Inst.LBU(9, 8, 0), # x9 = memory[x7]
    Inst.LBU(14, 13, 0), # x14 = memory[x11]
    Inst.SB(6, 9, 0),
    Inst.SB(12, 14, 0),
    Inst.LW(15, 12, 0x48), # offset 0x48取得
    Inst.ANDI(10, 15, 0x01), # Push判定
    Inst.LBEQ(10, 0, 'loop'), # 押されていないならloopに戻る
    Inst.ADDI(7, 7, 1), # x7++
    Inst.ADDI(10, 7, -0x0a), # x7 - 0x0a
    Inst.LBNE(10, 0, 'loop'), # 11を引いて0じゃなければloopに戻る
    Inst.ANDI(7, 7, 0x00000000), # clear
    Inst.ADDI(11, 11, 1), # x11++
    Inst.ADDI(10, 11, -0x0a), # x11 - 0x0a
    Inst.LBNE(10, 0, 'loop'), # 11を引いて0じゃなければloopに戻る
    Inst.ANDI(11, 11, 0x00000000), # clear
]

r = asm(program)
print_asm(r)
print()
print_ihex(r)