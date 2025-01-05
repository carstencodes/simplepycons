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


class JekyllIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "jekyll"

    @property
    def original_file_name(self) -> "str":
        return "jekyll.svg"

    @property
    def title(self) -> "str":
        return "Jekyll"

    @property
    def primary_color(self) -> "str":
        return "#CC0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Jekyll</title>
     <path d="M8.073 24c-.348
 0-.689-.063-1.02-.189-1.375-.525-2.104-2.02-1.726-3.402l-.015-.006.09-.226L12.399
 2.01c.105-.27.057-.91.006-1.267-.016-.085-.016-.161.008-.24l.008-.023.006-.015V.458l.009-.019c.108-.292.45-.439
 1.008-.439.673 0 1.602.21 2.551.573.797.307 1.523.689 2.033
 1.075.602.45.842.854.707
 1.2l-.031.045-.016.015c-.045.061-.09.12-.15.165-.314.271-.764.735-.84.945l-7.063
 18.421-.016-.006c-.494.948-1.457 1.557-2.543
 1.561H8.07l.003.006zm-2.187-3.718l-.02.05c-.447 1.201.162 2.557 1.364
 3.018.271.105.551.154.837.154.971 0 1.83-.585 2.188-1.5l.027-.061
 6.959-18.09c.146-.39.84-1.02.979-1.14l.016-.016c.012-.015.02-.015.02-.03
 0-.06-.061-.27-.557-.645-.479-.36-1.154-.72-1.904-1.005-.868-.328-1.768-.539-2.368-.539-.39
 0-.524.082-.545.126v.04c.016.104.147 1.035-.034 1.515l-6.962
 18.12v.003zm8.95-11.507s-.964 1.109-1.843
 1.509c-.88.398-1.529.293-2.32.756-.789.461-1.188 1.103-1.188
 1.103L6.27 20.505c-.348.944.168 2.05 1.125 2.42.96.369 2.04-.12
 2.412-1.056l5.029-13.094zM9.905 18.76c.104-.041.225 0
 .266.105.042.104 0 .222-.105.264-.104.043-.225 0-.266-.104-.042-.097
 0-.216.105-.265zm-1.014-1.802c-.152.068-.334 0-.397-.155-.07-.152
 0-.334.154-.397.154-.07.335 0
 .398.153.074.15.008.314-.155.39v.009zm.286-1.096c-.123-.288
 0-.623.287-.758.285-.124.615 0 .75.285.121.289 0
 .624-.285.757-.3.126-.629
 0-.765-.285l.013.001zm2.426-2.258c.153-.074.335 0 .398.15.07.154 0
 .336-.153.399-.155.07-.337 0-.399-.155-.074-.152
 0-.334.154-.397v.003zm-1.293-1.379c.105-.042.226 0 .266.105.043.104 0
 .226-.104.266-.104.042-.226
 0-.265-.104-.044-.106.006-.227.103-.267zM13.681 1.14c.1-.261.993-.162
 1.995.226.999.384 1.729.909 1.63
 1.17-.104.264-.997.164-1.996-.221-1.005-.385-1.734-.91-1.632-1.176h.003z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/jekyll/brand/blob/8302ad3e'''

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
