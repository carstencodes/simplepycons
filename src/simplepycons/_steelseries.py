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


class SteelseriesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "steelseries"

    @property
    def original_file_name(self) -> "str":
        return "steelseries.svg"

    @property
    def title(self) -> "str":
        return "Steelseries"

    @property
    def primary_color(self) -> "str":
        return "#FF5200"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Steelseries</title>
     <path d="M14.08008 0c-1.00234 0-1.8125.80893-1.8125
 1.8086v2.57226c-4.01871.7444-7.19505 3.9119-7.93946
 7.91992H1.8125c-1.001 0-1.8125.80698-1.8125 1.80664 0 .99833.8115
 1.8086 1.8125 1.8086h2.51563C5.18077 20.5094 9.22875 24 14.08008 24
 19.54884 24 24 19.56148 24
 14.10742c0-4.83662-3.50067-8.87524-8.10742-9.72656V1.80859C15.89258.80893
 15.08108 0 14.08008 0ZM4.69336 3.17578c-1.00368 0-1.8164.80955-1.8164
 1.81055 0 .99966.81272 1.8125 1.8164 1.8125 1.001 0 1.8164-.81284
 1.8164-1.8125 0-1.001-.8154-1.81055-1.8164-1.81055zm9.38672
 4.65625c3.46809 0 6.29297 2.81398 6.29297 6.2754 0 3.46006-2.82488
 6.27734-6.29297 6.27734-3.46943 0-6.29297-2.81728-6.29297-6.27735
 0-3.4614 2.82354-6.27539 6.29297-6.27539zm-.01758 2.4043c-2.14634
 0-3.89258 1.73986-3.89258 3.88086S11.91616 18 14.0625 18c2.14634 0
 3.89258-1.74182 3.89258-3.88281
 0-2.141-1.74624-3.88086-3.89258-3.88086zm0 2.7168c.6455 0
 1.16797.51989 1.16797 1.16406 0 .64283-.52246 1.16797-1.16797
 1.16797-.64417 0-1.16992-.52514-1.16992-1.16797
 0-.64417.52575-1.16407 1.16992-1.16407z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://techblog.steelseries.com/ux-guide/ind'''

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
