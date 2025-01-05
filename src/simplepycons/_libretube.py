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


class LibretubeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "libretube"

    @property
    def original_file_name(self) -> "str":
        return "libretube.svg"

    @property
    def title(self) -> "str":
        return "LibreTube"

    @property
    def primary_color(self) -> "str":
        return "#FF9699"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>LibreTube</title>
     <path d="M2.12 0c-.2688.004-.5138.2196-.5138.5206v4.9981c0
 .1875.1009.3604.2641.4525l9.8769 5.5768c.3522.199.3522.7062 0
 .9051L1.8703 18.03a.52.52 0 0 0-.264.4526v4.997c0
 .4016.436.6514.7824.4484L22.207 12.3121a.3777.3777 0 0
 0-.0003-.652L2.3883.072A.516.516 0 0 0 2.1199 0zm-.005
 7.9458c-.2671.006-.5088.2216-.5088.5203v7.056c0
 .3982.4296.6484.776.452l6.222-3.528c.3512-.199.3512-.705
 0-.904l-6.222-3.528a.515.515 0 0 0-.2674-.0683z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/libre-tube/libre-tube.gith
ub.io/blob/e5e10090cab71ee7c0abdfbf2789977025733eb7/assets/icons/icon.'''

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
