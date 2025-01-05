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


class CoppelIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "coppel"

    @property
    def original_file_name(self) -> "str":
        return "coppel.svg"

    @property
    def title(self) -> "str":
        return "Coppel"

    @property
    def primary_color(self) -> "str":
        return "#0266AE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Coppel</title>
     <path d="M.738 2.879a.716.716 0 0 0-.738.74v16.762c0
 .428.35.74.738.74h22.52a.739.739 0 0 0
 .739-.74V3.619c.039-.428-.31-.74-.738-.74Zm6.614 6.34c1.167 0 2.1.935
 2.1 2.101 0
 .234-.04.427-.079.621h12.058v1.868h-.973v2.527h-.97v-1.283h-.935v1.283h-.972v-2.527H9.373c.04.194.079.428.079.623a2.09
 2.09 0 0 1-2.1 2.1c-1.011 0-1.83-.7-2.063-1.634a3.388 3.388 0 0
 1-.62.077 2.092 2.092 0 0 1-2.102-2.1c0-1.167.934-2.1 2.101-2.1.234 0
 .427 0 .621.079.234-.934 1.052-1.635 2.063-1.635Zm0 1.168c-.545
 0-.973.428-.934.933 0 .506.428.932.934.932a.945.945 0 0 0
 .933-.932.947.947 0 0 0-.933-.933zM4.668 11.94a.947.947 0 0
 0-.933.934c0 .506.428.934.933.934a.947.947 0 0 0 .934-.934.947.947 0
 0 0-.934-.934zm2.684 1.518a.947.947 0 0 0-.934.934c0
 .505.428.933.934.933a.947.947 0 0 0 .933-.933.947.947 0 0
 0-.933-.934z" />
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
