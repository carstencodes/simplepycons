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


class CodefreshIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "codefresh"

    @property
    def original_file_name(self) -> "str":
        return "codefresh.svg"

    @property
    def title(self) -> "str":
        return "Codefresh"

    @property
    def primary_color(self) -> "str":
        return "#08B1AB"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Codefresh</title>
     <path d="M0 2.84c1.402 2.71 1.445 5.241 2.977 10.4 1.855 5.341
 8.703 5.701 9.21 5.711.46.726 1.513 1.704 3.926
 2.21l.268-1.272c-2.082-.436-2.844-1.239-3.106-1.68l-.005.006c.087-.484
 1.523-5.377-1.323-9.352C7.182 3.583 0 2.84 0 2.84zm24
 .84c-3.898.611-4.293-.92-11.473 3.093a11.879 11.879 0 0 1 2.625
 10.05c3.723-1.486 5.166-3.976 5.606-6.466 0 0 1.27-4.716
 3.242-6.677zM12.527 6.773l-.002-.002v.004l.002-.002zM2.643 5.22s5.422
 1.426 8.543 11.543c-2.945-.889-4.203-3.796-4.63-5.168h.006a15.863
 15.863 0 0 0-3.92-6.375z" />
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
