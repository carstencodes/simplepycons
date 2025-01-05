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


class DavinciResolveIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "davinciresolve"

    @property
    def original_file_name(self) -> "str":
        return "davinciresolve.svg"

    @property
    def title(self) -> "str":
        return "DaVinci Resolve"

    @property
    def primary_color(self) -> "str":
        return "#233A51"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>DaVinci Resolve</title>
     <path d="M17.621 0 5.977.004c-1.37 0-2.756.345-3.762 1.11a4.925
 4.925 0 0 0-1.61 2.003C.233 3.93 0 5.02 0 5.951l.012 12.2c.002
 1.604.479 3.057 1.461 4.112.984 1.056 2.462 1.683 4.331 1.691L16.856
 24c1.26.005 3.095-.036 4.303-.714 1.075-.605 2.025-1.556
 2.497-2.984.278-.84.345-2.084.344-3.147l-.021-11.13c-.002-.888-.15-2.023-.547-2.934-.425-.976-1.181-1.815-2.322-2.425C20.353.26
 19.123 0 17.622 0zm0 .93c1.378 0 2.538.295 3.04.565.977.523 1.544
 1.166 1.889 1.96.315.721.47 1.793.473 2.572l.018 11.13c.002
 1.013-.097 2.257-.298 2.86-.396 1.202-1.146 1.946-2.063
 2.462-.814.457-2.612.593-3.82.588l-11.05-.044c-1.657-.007-2.832-.534-3.626-1.386-.792-.851-1.212-2.06-1.212-3.485L.999
 5.95c0-.829.196-1.827.474-2.437.345-.757.75-1.207 1.365-1.674C3.585
 1.27 4.868.97 6.08.97zm-5.66 3.423c-1.976.089-3.204 1.658-3.214
 3.29.019 1.443 1.635 3.481 2.884
 4.53.12.099.154.109.33.18.062.025.198-.047.327-.135.36-.245.993-.947
 1.648-1.738a7.67 7.67 0 0 0
 1.031-1.683c.409-.89.261-1.599.235-1.888a3.983 3.983 0 0 0-.99-1.692
 3.36 3.36 0 0 0-2.251-.864zm4.172 7.922a10.185 10.185 0 0
 0-3.244.61c-.15.058-.26.1-.374.17-.057.036-.11.135-.105.292.017.433.29
 1.278.624 2.27.384 1.135 1.066 2.27 1.844 2.74a3.23 3.23 0 0 0
 2.53.342c.832-.243 1.595-.868
 1.962-1.546.986-1.818.19-3.548-1.121-4.417-.447-.296-1.133-.445-1.89-.46-.074
 0-.15-.002-.226-.001zm-8.432.038a6.201 6.201 0 0
 0-.752.047c-.596.078-.932.273-1.29.51a3.177 3.177 0 0 0-1.365
 1.979c-.075.552-.086 1.053.033 1.507.433 1.389 1.326 2.222 2.847
 2.452.636.028 1.37-.063 1.99-.45 1.269-.782 2.08-3.17
 2.412-4.742.053-.176.035-.357-.013-.42-.005-.067-.044-.113-.19-.183-.398-.192-1.32-.417-2.375-.6a7.68
 7.68 0 0 0-1.297-.1z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.blackmagicdesign.com/media/images'''

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
