from typing import List


def smallest_common_prefix(one: str, two: str) -> str:
    result = ""

    for a, b in zip(one, two):
        if a != b:
            return result
        result += a
    return result


def smallest_cidr_range(ips: List[str]) -> str:
    if len(ips) == 1:
        block = ips[0]
    else:
        block = smallest_common_prefix(ips[0], ips[len(ips) - 1])

    block_length = len(block)
    block = block.ljust(32, "0")

    smallest_block_ip = []
    for i in range(0, len(block), 8):
        smallest_block_ip.append(str(int(block[i : i + 8], 2)))

    return f"{'.'.join(smallest_block_ip)}/{block_length}"


def main():
    test_cases = int(input())

    for _ in range(test_cases):
        num_ips = int(input())

        ips = []
        for _ in range(num_ips):
            ips.append(
                "".join(bin(int(part))[2:].rjust(8, "0") for part in input().split("."))
            )

        print(smallest_cidr_range(sorted(ips)))


if __name__ == "__main__":
    main()
