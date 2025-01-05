#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class GitkrakenIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gitkraken"

    @property
    def original_file_name(self) -> "str":
        return "gitkraken.svg"

    @property
    def title(self) -> "str":
        return "GitKraken"

    @property
    def primary_color(self) -> "str":
        return "#179287"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>GitKraken</title>
     <path d="M23.225 6.252a.478.478 0 00-.923.171c0
 .053.013.119.026.171 2.15 5.71-.751 12.077-6.46 14.226a10.9 10.9 0
 01-2.426.607v-5.155c.33-.066.646-.158.962-.264v4.338c5.445-1.332
 8.794-6.817 7.463-12.262a10.147 10.147 0 00-4.958-6.487.472.472 0
 00-.646.185.472.472 0 00.185.646c4.443 2.452 6.051 8.056 3.6
 12.499a9.13 9.13 0 01-4.681 4.1v-3.836a1.472 1.472 0
 001.028-1.398c0-.527-.264-1.002-.725-1.266.343-3.309 1.859-2.439
 1.859-3.493v-.62c0-1.582-3.665-6.737-5.38-6.856h-.316c-1.714.119-5.379
 5.274-5.379 6.856v.62c0 1.054 1.503.184 1.859 3.493a1.461 1.461 0
 00-.725 1.266c0 .646.422 1.2 1.028 1.398v3.836C3.91 17.168 1.59 11.83
 3.448 7.11a9.24 9.24 0 014.1-4.68.479.479 0 00.185-.66.487.487 0
 00-.422-.237.444.444 0 00-.224.065 10.142 10.142 0 00-3.982 13.791
 10.147 10.147 0 006.487
 4.958V16.02c.316.106.633.198.962.264v5.155C4.503 20.636.257 15.085
 1.062 9.034a10.9 10.9 0 01.606-2.426.489.489 0 00-.277-.62.494.494 0
 00-.62.277c-2.333 6.21.805 13.131 7.015 15.452 1.2.448 2.452.699
 3.73.751v-6.09c.172.012.489.012.489.012s.316 0
 .488-.013v6.078c6.631-.277 11.773-5.867 11.496-12.499a12.458 12.458 0
 00-.764-3.704zm-9.019 6.842a.995.995 0 011.398 0 .995.995 0 010
 1.398.995.995 0 01-1.398 0 .988.988 0 010-1.398zm-4.43 1.398a.979.979
 0 01-1.384 0 .995.995 0 010-1.398.995.995 0 011.398 0 .983.983 0
 01-.013 1.398z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
