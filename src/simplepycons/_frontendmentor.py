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


class FrontendMentorIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "frontendmentor"

    @property
    def original_file_name(self) -> "str":
        return "frontendmentor.svg"

    @property
    def title(self) -> "str":
        return "Frontend Mentor"

    @property
    def primary_color(self) -> "str":
        return "#3F54A3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Frontend Mentor</title>
     <path d="M12.1706 1.2719a.732.732 0 00-.7186.732v13.914a.732.732
 0 00.732.732.732.732 0 00.7318-.732V2.004a.732.732 0
 00-.7452-.732zm11.0741 4.1685a.7339.7339 0 00-.2764.063L16.686
 8.307a.7329.7329 0 000 1.3361l6.2823 2.8134a.7378.7378 0
 00.2993.0648.732.732 0 00.2973-1.401l-4.786-2.1443
 4.786-2.1366a.7339.7339 0 00.3698-.9664.7339.7339 0
 00-.69-.4327zm-22.499 5.032a.7316.7316 0 00-.7223.9149c1.736 6.677
 7.7748 11.341 14.6822 11.341a.732.732 0 000-1.464 13.7055 13.7055 0
 01-13.266-10.2449.7316.7316 0 00-.6939-.547z" />
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
