import operator
from typing import Callable


def normalize_odds(home_odds: float, away_odds: float) -> tuple[float, float]:
    sum_ = home_odds + away_odds
    return home_odds / sum_, away_odds / sum_


def print_table(
    rows: list,
    get_stats: Callable[[], list[str]],
    header: list[str],
    sort: bool = False,
    sort_key: str = "",
    **header_kwargs,
) -> None:
    print_header(header, **header_kwargs)
    if sort:
        rows = list(reversed(sorted(rows, key=operator.attrgetter(sort_key))))
    for row in rows:
        print_row(get_stats(row))


def print_header(header: list[str], delimeter: str = "*", factor: int = 5) -> None:
    delimeter = [delimeter * factor] * len(header)
    print("\t".join(header))
    print("\t".join(delimeter))


def print_row(row: list[str]) -> None:
    print("\t".join(row))
